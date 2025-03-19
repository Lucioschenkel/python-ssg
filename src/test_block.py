import unittest

from block import block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
        tests = [
            (
                """
# This is a heading
""",
                BlockType.HEADING
            ),
            (
                """
> this
> is
> a
> quote
""",
                BlockType.QUOTE
            ),
            (
                """
- this
- is a
- list
""",
                BlockType.UNORDERED_LIST
            ),
            (
                """
1. this
2. is a
3. list
""",
                BlockType.ORDERED_LIST
            ),
            (
                """
```javascript
let a = 'something';
```
""",
                BlockType.CODE
            ),
            (
                "This is just a paragraph",
                BlockType.PARAGRAPH
            )

        ]
        for md, expected_type in tests:
            self.assertEqual(block_to_block_type(md), expected_type)

