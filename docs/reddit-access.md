# Reddit as a source: access status and limitations

*Last checked: 2026-11-19.*

**Status:** a Reddit collector (`aiconcerns/collectors/reddit.py`) is drafted but **disabled** (`sources.reddit.enabled: false`). No Reddit data has been collected, because no API credentials could be obtained. The rest of the pipeline (cleaning, classification, clustering, report) is unchanged and still YouTube-only.

## What was tested

| Test | Result |
|---|---|
| Registering a "script" app at `reddit.com/prefs/apps` (2026-11-19) | ❌ The form loops back to the reCAPTCHA; no app is created (see §1) |
| Reading the Responsible Builder Policy page | ❌ The help site returns HTTP 403 to automated requests; the policy points below are second-hand |
| Collector against **mocked** Reddit API responses (search listings + nested comment trees) | ✅ Posts outside the date range, NSFW posts and posts with too few comments are skipped. `[deleted]`/`[removed]` bodies are dropped. u/names, @handles, e-mails and URLs are stripped. Negative scores are clipped to 0. Nested replies are kept and "load more" stubs skipped. Subreddit searches use `restrict_sr` |
| Collector against the **live** API | ⏸️ Not run, because there are no credentials |
| Full pipeline with Reddit data (clean → classify → cluster → report) | ⏸️ Not run |

> **Caveat on sources.** Reddit's official policy page ([Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)) returns HTTP 403 to automated requests, so the points below come from a Reddit admin announcement in r/redditdev, user reports and third-party summaries, not the policy text itself. Read the official page and correct this file where it differs.

## 1. Credentials can't be self-registered

- **Observed here:** creating a "script" app at `reddit.com/prefs/apps` fails silently. After the reCAPTCHA, the form returns to the captcha and no app is created.
- **Why:** on 11 November 2025 Reddit introduced the Responsible Builder Policy and **closed self-service access** to the Data API. New OAuth credentials need a request that Reddit reviews. Apps created before the change keep working, which is why older guides still say to use `prefs/apps`.
- **Review:** an admin said Reddit aimed for about a 7-day turnaround on most tickets. Later reports say 2–4 weeks, with mixed outcomes and some quick rejections for requests that lacked detail.

## 2. Deadlines (reported, not verified against Reddit)

| Date | Reported change |
|---|---|
| 2025-11-11 | Self-service API access closed; Responsible Builder Policy introduced |
| 2026-09-30 | Existing app owners asked to register their apps |
| 2026-10-31 | **New requests for public Data API access no longer accepted** |
| 2026-11-13 | RSS feeds end |
| 2027-01-12 | Unregistered apps start losing access |
| 2027-03 | Public API access ends for all remaining apps and users |

If these dates are accurate, a new standard API app can't be requested any more. Even an approved app would lose public access in March 2027, so Reddit is a poor long-term source.

## 3. The policy may not permit this pipeline's use even with access

Reported policy points that conflict with how this project uses data:

| Policy point (as reported) | Conflict with this pipeline |
|---|---|
| Research using Reddit data collected outside the **Reddit for Researchers (RFR)** program violates the policy | This project is research; the policy's intended route is RFR, not a standard app |
| No sharing or commercialising Reddit data, or using it with ML/AI models, without written approval | Every text is sent to Claude (Haiku to classify, Opus to label), and the anonymised corpus and quotes are published in this repo |
| No deriving or inferring sensitive characteristics of users (e.g. health, political affiliation) | The pipeline groups opinions, not users, but r/PolskaPolityka and the health and politics themes are close to this line |
| Delete user data on request; report data leaks | The committed `data/corpus.sqlite` would need a deletion process for Reddit items |

## 4. Possible ways forward

| Route | Assessment |
|---|---|
| Standard API app request | Reportedly closed since 2026-10-31, and may not cover this use anyway |
| **Reddit for Researchers** ([r/reddit4researchers](https://www.reddit.com/r/reddit4researchers/)) | **The only sanctioned route for this project.** Aimed at academic researchers, so eligibility for an independent project is uncertain |
| Devvit | Not suitable: apps run inside subreddits where they're installed (moderator approval needed), use Devvit's own API client, and are restricted from sending data off-platform. Devvit doesn't give credentials the collector can use |
| Scraping with a browser | **Not used.** Breaks Reddit's terms (Reddit has sued scrapers), risks account and IP bans, and gives incomplete data. Publishing the resulting corpus would also make a GDPR research-exemption argument weaker. |

## 5. If access is granted

1. Put the credentials in `.env` as `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` (optionally `REDDIT_USER_AGENT`), and set `sources.reddit.enabled: true`.
2. Check the approval's terms against §3. In particular, check whether sending texts to an LLM and publishing the anonymised corpus and quotes are allowed. If they aren't, keep Reddit items out of the committed `data/corpus.sqlite` and out of the published quotes.
3. Do a small run first (e.g. `sources.reddit.max_posts: 5`), check `data/collect.log`, then run the full pipeline.
4. Adjust the YouTube-specific parts:
   - the classifier prompt in `aiconcerns/llm.py` says comments are under a "film" (video);
   - the report's caveats and its "1 video" column (`aiconcerns/report.py`) assume videos;
   - the README's privacy section should mention Reddit.
   A per-source share column in the theme table would also show where a theme comes mostly from one platform.

**Known collector limitations:**
- Comments behind "load more" stubs aren't expanded.
- Posts that are only a short title (under `cleaning.min_words`) are dropped.
- Downvoted items get engagement 0.
- NSFW posts and posts with fewer than `min_comments` comments are skipped.

## Sources

- [r/redditdev: Introducing the Responsible Builder Policy (Reddit admin, 2025-11-11)](https://www.reddit.com/r/redditdev/comments/1oug31u/introducing_the_responsible_builder_policy_new/)
- [r/redditdev: "Create app" button does nothing, silent failure (2026-01)](https://www.reddit.com/r/redditdev/comments/1qf7707/create_app_button_does_nothing_silent_failure_new/)
- [r/reddit4researchers: Apply to join the Reddit for Researchers beta](https://www.reddit.com/r/reddit4researchers/comments/1egr9wu/apply_to_join_the_reddit_for_researchers_beta_by)
- [Reddit Data API October 31 cutoff (redditapis.com)](https://www.redditapis.com/blogs/reddit-data-api-october-31-cutoff-2026)
- [Reddit Data API in 2026: access and alternatives (redditapis.com)](https://www.redditapis.com/blogs/reddit-data-api-2026)
- [Reddit API shutdown: the dates and what still works (looot.ai)](https://looot.ai/blog/reddit-api-shutdown)
- [Reddit Data API Terms & Commercial Use (prowlo.com)](https://prowlo.com/blog/reddit-data-api)
- [Reddit API Access in 2026: How to Get Started (Activepieces)](https://www.activepieces.com/blog/reddit-api-access-in-2026-how-to-get-started)
