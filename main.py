/****************** PART 1 ******************/
% Creating binary trees with symbols and their ASCII codes
declare
fun {Ascii_16}
   tree(
      leaf(32#20 ' ')
      leaf(32#41 'A') leaf(32#42 'B') leaf(32#43 'C') leaf(32#44 'D') leaf(32#45 'E')
      leaf(32#46 'F') leaf(32#47 'G') leaf(32#48 'H') leaf(32#49 'I') leaf(32#4A 'J')
      leaf(32#4B 'K') leaf(32#4C 'L') leaf(32#4D 'M') leaf(32#4E 'N') leaf(32#4F 'O')
      leaf(32#50 'P') leaf(32#51 'Q') leaf(32#52 'R') leaf(32#53 'S') leaf(32#54 'T')
      leaf(32#55 'U') leaf(32#56 'V') leaf(32#57 'W') leaf(32#58 'X') leaf(32#59 'Y')
      leaf(32#5A 'Z') leaf(32#61 'a') leaf(32#62 'b') leaf(32#63 'c') leaf(32#64 'd')
      leaf(32#65 'e') leaf(32#66 'f') leaf(32#67 'g') leaf(32#68 'h') leaf(32#69 'i')
      leaf(32#6A 'j') leaf(32#6B 'k') leaf(32#6C 'l') leaf(32#6D 'm') leaf(32#6E 'n')
      leaf(32#6F 'o') leaf(32#70 'p') leaf(32#71 'q') leaf(32#72 'r') leaf(32#73 's')
      leaf(32#74 't') leaf(32#75 'u') leaf(32#76 'v') leaf(32#77 'w') leaf(32#78 'x')
      leaf(32#79 'y') leaf(32#7A 'z')
   )
end

fun {Ascii_2}
   tree(
      leaf(0b0100000 ' ')
      leaf(0b1000001 'A') leaf(0b1000010 'B') leaf(0b1000011 'C') leaf(0b1000100 'D') leaf(0b1000101 'E')
      leaf(0b1000110 'F') leaf(0b1000111 'G') leaf(0b1001000 'H') leaf(0b1001001 'I') leaf(0b1001010 'J')
      leaf(0b1001011 'K') leaf(0b1001100 'L') leaf(0b1001101 'M') leaf(0b1001110 'N') leaf(0b1001111 'O')
      leaf(0b1010000 'P') leaf(0b1010001 'Q') leaf(0b1010010 'R') leaf(0b1010011 'S') leaf(0b1010100 'T')
      leaf(0b1010101 'U') leaf(0b1010110 'V') leaf(0b1010111 'W') leaf(0b1011000 'X') leaf(0b1011001 'Y')
      leaf(0b1011010 'Z') leaf(0b1100001 'a') leaf(0b1100010 'b') leaf(0b1100011 'c') leaf(0b1100100 'd')
      leaf(0b1100101 'e') leaf(0b1100110 'f') leaf(0b1100111 'g') leaf(0b1101000 'h') leaf(0b1101001 'i')
      leaf(0b1101010 'j') leaf(0b1101011 'k') leaf(0b1101100 'l') leaf(0b1101101 'm') leaf(0b1101110 'n')
      leaf(0b1101111 'o') leaf(0b1110000 'p') leaf(0b1110001 'q') leaf(0b1110010 'r') leaf(0b1110011 's')
      leaf(0b1110100 't') leaf(0b1110101 'u') leaf(0b1110110 'v') leaf(0b1110111 'w') leaf(0b1111000 'x')
      leaf(0b1111001 'y') leaf(0b1111010 'z')
   )
end

/****************** PART 2 ******************/
% Calculate the frequency of each symbol in a list
declare
fun {Sym_Freq Sym L}
   case L
   of nil then 0
   [] H|T andthen H == Sym then 1 + {Sym_Freq Sym T}
   [] _|T then {Sym_Freq Sym T}
   end
end

/****************** PART 3 ******************/
% Compress the sequence with base 16
declare
fun {Compress_16 L}
   case L
   of nil then nil
   [] H|T then {Atom.toHexString {Ascii_16 H}} | {Compress_16 T}
   end
end

/****************** PART 4 ******************/
% Uncompress the sequence with base 2
declare
fun {Uncompress_2 L}
   case L
   of nil then nil
   [] H|T then {Ascii_2 {Atom.toBits H}} | {Uncompress_2 T}
   end
end

/************* Functional Programming Solution *************/

/* Defining a binary tree for storing symbol-frequency pairs */
declare
fun {MakeLeaf Symbol Freq}
   leaf(Symbol#Freq)
end

fun {MakeNode Left Right}
   tree(Left Right)
end

/* Function to insert a symbol-frequency pair into the binary tree */
fun {Insert Symbol Freq Tree}
   case Tree
   of leaf then {MakeNode {MakeLeaf Symbol Freq} leaf}
   [] tree(L R) then
      if Freq =< L.2 then
         {MakeNode {Insert Symbol Freq L} R}
      else
         {MakeNode L {Insert Symbol Freq R}}
      end
   end
end

/* Function to build the frequency table (symbol-frequency pairs) */
fun {BuildFreqTable L}
   fun {FreqAcc Sym L Acc}
      case L
      of nil then Acc
      [] H|T andthen H == Sym then {FreqAcc Sym T Acc+1}
      [] _|T then {FreqAcc Sym T Acc}
      end
   end
   fun {FreqList L Acc}
      case L
      of nil then Acc
      [] H|T then {FreqList T Acc#(H#{FreqAcc H L 0})}
      end
   end
in
   {FreqList L nil}
end

/* Function to construct the Huffman tree from the frequency table */
fun {BuildHuffmanTree FreqTable}
   fun {InsertAll Tree FreqTable}
      case FreqTable
      of nil then Tree
      [] H|T then {InsertAll {Insert H.1 H.2 Tree} T}
      end
   end
in
   {InsertAll leaf FreqTable}
end

/************* Example Usage *************/

/* Example sequence from Fig 1 */
declare ExampleSequence = [&t &h &i &s &i &s &a &n &e &x &a &m &p &l &e &o &f &a &h &u &f &f &m &a &n &t &r &e &e]

/* Build the frequency table */
declare FreqTable = {BuildFreqTable ExampleSequence}

/* Build the Huffman tree */
declare HuffmanTree = {BuildHuffmanTree FreqTable}

/* Browse the resulting Huffman tree */
{Browse Huffman