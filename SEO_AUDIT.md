# SEO Audit – On Call Notary

## Snapshot (current repo state)
- **Strengths:** Local-focused copy, city landing pages, FAQ schema on home, sitemap & robots already present.
- **Gaps discovered:**
  - Many pages lacked modern social preview metadata (OpenGraph/Twitter) and consistent canonicals on the main funnels (home/services/contact/areas/jail pages).
  - LocalBusiness schema existed only on home and was missing geo coordinates, service taxonomy, and contactPoint details.
  - Secondary pages didn’t describe themselves to crawlers (no Collection/Contact/Service schemas or breadcrumbs), reducing relevance signals and sitelink odds.
  - Legacy references to `oncallnotarysb.com` remain across city/jail pages and email addresses; they should be aligned to your primary domain to prevent duplicate indexing and user confusion.

## Changes made in this pass
- Added OpenGraph/Twitter previews, robots directives, and canonicals to top-level funnels (home, services, contact, areas-served, jail-notary) for consistent indexing and richer link previews.
- Expanded structured data: enhanced LocalBusiness (geo + service areas + contactPoint), added Service schemas for core offerings, ContactPage schema, CollectionPage + breadcrumbs for Areas Served, and a dedicated Jail Notary Service entity.

## Highest-impact next steps
1. **Unify domain signals**
   - Update remaining pages (all city pages, jail subpages, service subpages) to use `https://oncallnotary.org` for canonicals, `og:url`, and schema `@id` values.
   - Replace email addresses if the official inbox has moved off `oncallnotarysb.com`, or add forwarding.

2. **Page speed & Core Web Vitals**
   - Compress hero/feature images and serve WebP/AVIF variants; preload the hero image used on multiple pages.
   - Inline only the minimal above-the-fold CSS and defer non-critical CSS/JS (especially icon fonts) to cut LCP.

3. **Content & intent coverage**
   - Add slim FAQ sections with FAQPage schema to services and contact pages (pricing, availability, ID requirements, acceptable payment) to win rich results.
   - Create unique, intent-matched intros for each city page (add landmarks/ZIP coverage and travel ETA expectations).
   - Add trust indicators near CTAs (NNA certification, bond/insurance, same-day guarantee) with click-to-call buttons.

4. **Technical hygiene**
   - Implement `hreflang` only if you publish Spanish pages; otherwise omit.
   - Ensure sitemap lists every live page (city and jail subpages) and regenerate after canonical updates.
   - Add GA/Ads conversion events to phone links (`tel:`) and “Book Now” buttons (currently only contact.html is tracked via `contact.html` link clicks).

5. **Local prominence**
   - Embed a static Google Map or “Serving San Bernardino County” badge with NAP consistency that matches your GMB.
   - Encourage Google/ Yelp review acquisition and link the primary review URL near the header/footer CTA.

6. **Accessibility/CTR boosts**
   - Ensure every image has descriptive `alt` text (logo, service imagery, detention-center photos).
   - Use descriptive anchor text for internal links (e.g., “mobile notary in Rialto” instead of “click here”).

## Measurement plan
- Track call clicks (`tel:+19097518439`), contact form submits, and scroll depth to hero CTA as primary events.
- Monitor Search Console for canonical/duplicate warnings after domain alignment.
- Run weekly PageSpeed Insights/Lighthouse for home, services, and a representative city page; log scores to watch CLS/LCP trends.

## Suggested weekly checklist
- Publish at least one micro-post (50–100 words) on new use-cases (e.g., hospital notarization tips) and link to the relevant service page.
- Rotate homepage hero with seasonal offers (after-hours availability, weekend surcharge waived) and update meta descriptions to reflect active promos.
- Verify NAP consistency across social profiles linked in the footer (Facebook/Instagram/Yelp) and update URLs if handles change.
