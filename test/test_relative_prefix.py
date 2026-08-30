import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from bulk_page_generation import generate_pages_recursive, relative_prefix_from_page


class TestRelativePrefixFromPage(unittest.TestCase):
    def test_nested_blog_page_uses_site_root_prefix(self):
        docs_root = Path('/tmp/site/docs')
        page_path = Path('/tmp/site/docs/blog/gandalf')

        self.assertEqual(relative_prefix_from_page(page_path, docs_root), '../../')

    def test_root_page_uses_current_directory_prefix(self):
        docs_root = Path('/tmp/site/docs')
        page_path = Path('/tmp/site/docs')

        self.assertEqual(relative_prefix_from_page(page_path, docs_root), './')

    def test_generated_blog_page_uses_site_root_asset_paths(self):
        with TemporaryDirectory() as tmpdir:
            base = Path(tmpdir)
            content_dir = base / 'content' / 'blog' / 'gandalf'
            content_dir.mkdir(parents=True)
            (content_dir / 'index.md').write_text('# Gandalf\n\n![Picture](/images/gandalf.png)')
            (base / 'docs').mkdir()
            (base / 'template.html').write_text('<link href="/index.css" rel="stylesheet" /><article>{{ Content }}</article>')

            generate_pages_recursive(base / 'content', base / 'template.html', base / 'docs')

            html = (base / 'docs' / 'blog' / 'gandalf' / 'index.html').read_text()
            self.assertIn('href="../../index.css"', html)
            self.assertIn('src="../../images/gandalf.png"', html)
