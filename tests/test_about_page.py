#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.link_crawler import LinkCrawler


class TestAboutPage:

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_about_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('about/', id='about-text')
        urls = urls + crawler.collect_links('about/', id='about-navigation')
        bad_urls = []

        Assert.greater(
            len(urls), 0, u'something went wrong. no links found.')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            u'%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
