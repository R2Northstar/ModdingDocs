from pygments.lexer import RegexLexer, words, include, default, bygroups, using, this
from pygments.token import (
    Text,
    Generic,
    Keyword,
    String,
    Name,
    Comment,
    Number,
    Operator,
    Punctuation,
    Whitespace,
    Token,
)

# test: py -m pygments -v -x -f html -O full,debug_token_types -l pygments-squirrel/lexer.py:SquirrelLexer sq.gnut > test.html; start test.html


class SquirrelLexer(RegexLexer):
    name = "Squirrel"
    aliases = ["squirrel"]
    filenames = ["*.nut", "*.gnut"]

    _keyword_types = [
        "void",
        "bool",
        "int",
        "float",
        "entity",
        "string",
        "vector",
        "asset",
        "var",
    ]
    _builtin_names = [
        "TitanLoadoutDef",
        "PilotLoadoutDef",
    ]
    _declarations = [
        "global",
        "const",
        "static",
        "local",
    ]
    tokens = {
        "values": [
            (r"[^\S\n]+", Whitespace),
            (r"(\"(\\.|.)*?[\"\n])", String),
            (r"-?([0-9]+(([.]([0-9]+)?)(e[-]?[0-9]+)?))", Number.Float),
            (r"(0x[0-9a-fA-F]+|0[0-7]+|-?[0-9]+|'[a-f]')", Number.Integer),
            include("constants"),
        ],
        "value": [include("values"), default("#pop")],
        "root": [
            (r"(\"(\\.|.)*?[\"\n])", String),
            include("comments"),
            include("keywords"),
            include("operators"),
            include("statement"),
            # include("generic"),
        ],
        "statement": [
            (r"#.*", Comment.Preproc),
            (r"(function)(\s+)", bygroups(Keyword, Whitespace), "funcname"),
            (r"(class)(\s+)", bygroups(Keyword, Whitespace), "classname"),
            include("declarations"),
            (r"struct", Name.Class),
            (r"enum", Name.Class),
            (
                r"(\.?)([a-zA-Z_]\w*)(\s*?)(\()",
                bygroups(Punctuation, Name.Function, Whitespace, Punctuation),
                "arguments",
            ),
            include("type"),
            (r"(?<=\w)(\.\w+)", Name.Attribute),
            (
                r"([a-zA-Z_]\w*)(\s*)(=)",
                bygroups(Name.Variable, Whitespace, Punctuation),
            ),
            include("values"),
            (r"[a-zA-Z_.]\w*", Name.Variable),
        ],
        "funcname": [
            (r"[a-zA-Z_]\w*", Name.Function),
            (r"[(]", Punctuation, "sig"),
            default("#pop"),
        ],
        "sig": [
            (
                r"(?<=[,(])(\s*?)(?=[a-zA-Z_]\w*\s*?[,)])",
                # only one type, not type space name (note: what did i mean?)
                bygroups(Whitespace),
                "typeb",
            ),
            (
                r"([a-zA-Z_]\w*)(\s*?)(?=[,)])",
                bygroups(Name.Variable, Whitespace),
            ),
            (r",", Punctuation),
            (r"=", Punctuation, "value"),
            (r"[)]", Punctuation, "#pop"),
            include("typed_name"),
        ],
        "itype": [
            (r"[>]", Punctuation, "#pop"),
            include("typed_name"),
        ],
        "typeb": [
            include("typed_name"),
            default("#pop"),
        ],
        "typed_name": [
            include("type"),
            (r"[a-zA-Z_]\w*", Generic.Error),
        ],
        "type": [
            (
                r"(array|table)(\s*?)(<)",
                bygroups(Keyword.Type, Whitespace, Punctuation),
                "itype",
            ),
            (words(_keyword_types, suffix=r"\b"), Keyword.Type),
            (words(_builtin_names, suffix=r"\b"), Name.Builtin),
            (
                r"(\s*?)(functionref)(\()",
                bygroups(Whitespace, Name.Builtin.Type, Punctuation),
                "sig",
            ),
            (",", Punctuation),
            include("whitespace"),
        ],
        "classname": [(r"[a-zA-Z_]\w*", Name.Class, "#pop")],
        "whitespace": [
            (r"\n", Whitespace),
            (r"[^\S\n]+", Whitespace),
        ],
        "arguments": [
            (r"\)", Punctuation, "#pop"),  # end of arguments
            (r"(,)", Punctuation),  # end of argument
            (r"\[", Punctuation, "array"),
            (r"{", Punctuation, "structure"),
            include("operators"),
            include("values"),
            # (r"[a-zA-Z_]\w*", Name.Variable),
            include("namedargs"),
        ],
        "namedargs": [(r"(\w+?)(=)", bygroups(Name.Variable, Punctuation))],
        "structure": [
            (r"}", Punctuation, "#pop"),  # end of structure
            (r"(,)( )", bygroups(Punctuation, Whitespace)),  # end of member
            (r"\[", Punctuation, "array"),
            include("namedargs"),
            (r"\.\.\.", Punctuation),
        ],
        "array": [
            (r"\]", Punctuation, "#pop"),
            (r"(,)( )", bygroups(Punctuation, Whitespace)),  # end of member
            (r" ", Whitespace),  # end of member
            (r"/\*.+?\*/", Comment),
        ],
        "comments": [
            (r"(//.*?$)", Comment.Single),
            (r"/\*", Comment.Multiline, "comment_multiline"),
        ],
        "comment_multiline": [
            (r"[^*/]", Comment.Multiline),
            (r"/\*", Comment.Multiline, "#push"),
            (r"\*/", Comment.Multiline, "#pop"),
            (r"[*/]", Comment.Multiline),
        ],
        "operators": [
            (words(("in", "and", "or", "not"), suffix=r"\b"), Operator.Word),
            (
                words(
                    (
                        "!",
                        "!=",
                        "||",
                        "==",
                        "&&",
                        "<=",
                        "=>",
                        "> ",
                        "+",
                        "+=",
                        "-",
                        "-=",
                        "/",
                        "/=",
                        "*",
                        "*= ",
                        "%",
                        "%=",
                        "++",
                        "--",
                        "<-",
                        "&",
                        "^ ",
                        "|",
                        "~",
                        ">>",
                        "<<",
                        ">>>",
                        "!",
                    ),
                ),
                Operator,
            ),
        ],
        "declarations": [
            (words(_declarations, suffix=r"\b"), Keyword.Declaration),
        ],
        "constants": [
            (
                words(
                    (
                        "true",
                        "false",
                        "null",
                    ),
                    suffix=r"\b",
                ),
                Keyword.Constant,
            ),
        ],
        "keywords": [
            (
                words(
                    (
                        "break",
                        "case",
                        "catch",
                        "clone",
                        "continue",
                        "default",
                        "delegate",
                        "delete",
                        "else",
                        "extends",
                        "for",
                        "foreach",
                        "if",
                        "local",
                        "resume",
                        "return",
                        "switch",
                        "this",
                        "throw",
                        "try",
                        "typeof",
                        "while",
                        "parent",
                        "yield",
                        "vargc",
                        "vargv",
                        "instanceof",
                        "static",
                        "untyped",
                        "globalize_all_functions",
                        "wait",
                        "thread",
                        "unreachable",
                        "expect",
                    ),
                    suffix=r"\b",
                ),
                Keyword,
            ),
            include("declarations"),
            include("constants"),
        ],
    }
