from block_type import BlockType, block_to_block_type
import unittest

class TestBlockType(unittest.TestCase):
    def test_block_type(self):
        block = "This is a normal paragraph with stripped whitespaces"
        result = block_to_block_type(block)
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)

        block = "###### The Heading"
        result = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(result, expected)

        block = '```\ntext = "text"\ntxet = text[::-1]```'
        result = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(result, expected)

        block = '> this is a quote\n>this is a second quote'
        result = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(result, expected)

        block = '- This is the first\n- this is the second\n- This is the third'
        result = block_to_block_type(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(result, expected)

        block = '1. This is the first\n2. this is the second\n3. This is the third'
        result = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(result, expected)