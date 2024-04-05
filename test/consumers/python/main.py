import tree_sitter_tlaplus as tstla
from tree_sitter import Language, Parser

TLAPLUS_LANGUAGE = Language(tstla.language(), 'tlaplus')
parser = Parser()
parser.set_language(TLAPLUS_LANGUAGE)
tree = parser.parse(bytes("""
---- MODULE Test ----
op ≜ ∀ n ∈ ℕ : n ≥ 0
====
""", "utf8"))
print(tree.root_node.sexp())

query = TLAPLUS_LANGUAGE.query('(def_eq) @capture')
for node, capture_name in query.captures(tree.root_node):
    print(node)

