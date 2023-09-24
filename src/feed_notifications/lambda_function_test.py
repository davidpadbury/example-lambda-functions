import unittest

from lambda_function import create_notification, fetch_new_entries

example_rss_file = 'example.rss.xml'

class FeedNotificationsTest(unittest.TestCase):
    def test_fetch_new_entries_returns_all(self):
        new_entries = fetch_new_entries(example_rss_file)

        self.assertEqual('Recent Announcements', new_entries.feed_name)
        self.assertGreater(len(new_entries.entries), 0)


    def test_fetch_new_entries_with_pubished_filter(self):
        all_entries = fetch_new_entries(example_rss_file)

        some_entry_published_date = all_entries.entries[50].published_parsed

        filtered_entries = fetch_new_entries(
            example_rss_file,
            since_published_date=some_entry_published_date
        )

        self.assertEqual(49, len(filtered_entries.entries))

    def test_create_notification(self):
        new_entries = fetch_new_entries(example_rss_file)
        entry = new_entries.entries[0]
        notification = create_notification(entry, new_entries.feed_name)

        self.assertEqual('AWS Trusted Advisor adds 1 new fault tolerance check', notification['title'])
        self.assertTrue(notification['description'].startswith('AWS Trusted Advisor now supports a'))


if __name__ == '__main__':
    unittest.main()