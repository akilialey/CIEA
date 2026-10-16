# CIEA website design critique

Method: two independent reviews, one by a design reviewer and one by the automated design checker with a browser check. 16 October 2026.

## The short answer

**Partly.** Your colours are not the problem. The site feels young because it piles playful effects on top of each other. Each one is fine alone, but together they say "summer camp" more than "trusted education partner". Bricolage Grotesque adds to it: it has been used on countless startup templates since 2023, and at heavy weights it looks soft and bubbly.

The good news is that the fix is mostly taking things away. The island feel can come from photography, the water and the colours instead of from decoration.

## Score

**Usability score: 21 out of 32 (66%, Acceptable).** Two of the ten checks (shortcuts for power users, and help documentation) don't apply to a marketing site, so the total is out of 32.

| # | Check | Score | Main issue |
|---|---|---|---|
| 1 | Shows what's happening | 3 | Navigation shows where you are. The contact form has nowhere to send yet. |
| 2 | Speaks the visitor's language | 3 | Plain language throughout. "Miscellaneous stand-alone services" reads as jargon. |
| 3 | Visitor stays in control | 3 | Normal navigation. The moving ticker can't be paused. |
| 4 | Consistency | 3 | Card colours carry no meaning, and "For Parents" lands on the About page. |
| 5 | Prevents mistakes | 2 | The form checks fields, but the phone and email are still placeholders. |
| 6 | Easy to recognise | 3 | Cards are clear, but every card says "Learn more". |
| 7 | Shortcuts | n/a | Doesn't apply to a marketing site. |
| 8 | Clean, focused design | 2 | Too many decorative effects compete for attention. |
| 9 | Recovering from mistakes | 2 | The form's error and success states are basic. |
| 10 | Help | n/a | The FAQ covers it well. |

## What makes it look juvenile, most to least

1. **The six pastel service cards** (butter, sky, pink, mint, peach) with corner blobs. This is the strongest "kids' app" signal on the site.
2. **The tilted photos with thick white borders and coloured circles behind them.** They read as a scrapbook, and the same frame repeats in every page header.
3. **The tilted, scrolling gold ticker** under the hero. It feels like a fairground banner.
4. **The rainbow pill chips** in the "Perhaps You Only Need ONE Service" section.
5. **The orange tilted seal** ("Co-creators of Barbados Study Tours"). It looks like a sticker rather than a credential, which undersells a real achievement.
6. **Very rounded corners on almost everything.** The site uses 8 different corner sizes.
7. **The headline font**, set very heavy and very large.
8. **Some photo choices.** The young children on Summer Camps say "kids' camp" to a university, and the stock turtle says "holiday".

## What's working, and should stay

- **The colours.** They come from your logo and feel Caribbean without cliché.
- **The "Why Choose Barbados?" section.** Its ruled two-column list is the most credible part of the site. Its style should spread to the rest.
- **The live water in the hero.** It belongs to CIEA alone. Keep it.

## The font

Your logo's wordmark is set in spaced serif capitals, but the website speaks in a completely different voice. A serif headline would tie the site to the brand and signal "education, established" to parents and universities.

| Option | Feel |
|---|---|
| **Fraunces + Figtree (recommended)** | Warm, literary, a soft curl that suits the island. Feels established, like a heritage hotel. Echoes your logo. |
| Young Serif + Figtree | Editorial and confident. More institutional, a little less warm. |
| Instrument Serif + Instrument Sans | Elegant and current, but thin. Works only at large sizes. |

All three are free Google Fonts. Figtree, the body font, stays.

## Priority fixes

**P0. Replace the pastel cards and rainbow chips** with one calm card style or a ruled list: white or deep blue, a small line icon, no tints or blobs.

**P1. Straighten the photography.** No tilt, no white borders, no circles behind photos. Use one large, straight photo per section with softer 8 to 12px corners. Turn the seal into a quiet line of text near the About heading.

**P1. Change the headline font** to Fraunces at a medium weight, slightly smaller (about 3.6rem instead of 4.4rem).

**P1. Give universities a path.** Today a study-abroad coordinator finds no page written for them. A "For Institutions" page would help (what you handle, how groups work, how to enquire). This needs your words; I won't write claims for you.

**P2. Calm the motion and colour.** Stop the ticker tilting and scrolling (a still row of the four programs works better). Use orange only for the main button, gold once per page, and retire the hibiscus pink. Swap the young-children and turtle photos for older students and real places.

## How the three audiences see it today

- **A parent, paying and cautious:** sees no face (Patricia's portrait is still a placeholder), no safeguarding or emergency information, and the sticker-and-pastel look hints at a small hobby business. "For Parents" just drops them on About.
- **A university coordinator:** finds nothing about group logistics, insurance or how a trip runs. The playful look suggests a youth tour operator, not a professional partner.
- **A 17-year-old on a phone:** has to scroll through two paragraphs before the buttons, the photo stack takes a full screen, and WhatsApp (your main channel) isn't visible straight away.

## Automated checker notes

The checker found 71 items. Most are deliberate design choices, not bugs:
- **Full-width sections.** Flagged as having no padding, but their inner containers carry it.
- **The ticker.** Flagged as motion, and it is intentional.
- **"World-class".** Flagged as a buzzword, but it's your copy, so it stays.

Three findings are real:
1. **Green footer headings** on blue are just under the contrast standard (4.4 against 4.5).
2. **Small headings on Study in Barbados** are too close in size to body text.
3. **One quote** has tight line spacing.

## Questions worth asking

1. If the site lost every colour except deep blue and white, would it still feel Caribbean? If not, the island feel is living in decoration rather than in the photos and the voice.
2. Who signs the cheque: the parent or the university? Should the home page speak to one first and give the other its own page?
3. The logo already speaks in serif capitals. Why should the website sound different?
