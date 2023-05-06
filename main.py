from optimized_ukkonen import ukkonen_v2, MIN_ASCII, MAX_ASCII
from optimized_ukkonen_v3 import ukkonen_v3, Node

from pprint import pprint

# from elias import elias_encode, elias_decode, decimal_to_bitarray
#
# encoded = elias_encode(561)
# print(encoded)
# # print(decimal_to_bitarray(112))
#
# print(elias_decode(encoded))


# for visualization purposes
# def getinfo_tree(root):
#     return getinfo_tree_aux(root)
#
#
# def getinfo_tree_aux(node):
#
#     result = [(node.start, str(node.end)), {}]
#
#     for idx, connected_node in enumerate(node.edges):
#         if isinstance(connected_node, Node):
#             result[1][chr(idx+MIN_ASCII)] = getinfo_tree_aux(connected_node)
#
#     return result
#
#
# def getinfo_tree_aux_v2(node, text):
#
#     if node.start is None:
#         result = [[], []]
#     else:
#         result = [text[node.start+1: int(str(node.end))+1], []]
#
#     for idx, connected_node in enumerate(node.edges):
#         if isinstance(connected_node, Node):
#             result[1].append([chr(idx+MIN_ASCII), getinfo_tree_aux_v2(connected_node, text)])
#
#     if len(result[-1]) == 0:
#         result.pop()
#
#     return result


if __name__ == "__main__":
    # text = "abab": this exmples does not require suffix link active node
    # text = "abcabxabcyab" # creates one suffix link and uses it
    text = "mississippissipg$"  # this example requires suffix link
    # text = "missippimippimmisi$"
    root = ukkonen_v3(text)

    # pprint(getinfo_tree(root))

    # pprint(getinfo_tree_aux_v2(root, text))

# case 1: there is no start/end
# if current_node.start == current_node.end and i-k+1 > 1:
#     previous_node.start = k+1
#     previous_node.end = i
#     break