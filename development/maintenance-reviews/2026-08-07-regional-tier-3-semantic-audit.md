# Maintenance Review: 2026-08-07 Regional Tier 3 Semantic Audit

## Scope and authority boundary

- **Audit ID:** `MAINT-2026-08-07-REGIONAL-TIER-3-SEMANTIC-AUDIT`
- **Objective:** Determine whether the complete accepted corpus forms a
  coherent regional model across physical geography, geology, climate,
  hydrology, ecology, organisms, settlement, economy, government, story
  knowledge, development records, and provenance.
- **Authority:** Audit-only routine process maintenance. This report records
  findings and recommendations; it grants no lore, story, design, or policy
  authority.
- **Session handling:** Direct audit of the accepted repository state. No
  intake case, submission, addendum, claim disposition, or canon change was
  created.
- **Branch:** `agent/regional-tier-3-semantic-audit`
- **Permitted change:** This maintenance report only.

This audit may identify contradictions, tensions, unsupported dependencies,
duplicated authority, provenance or linkage defects, boundary leaks, stale
records, and coherent relationships. It does not decide which competing claim
is correct, infer a missing mechanism, answer an open question, promote
working material, establish an alias, change repository governance, or alter
any authority-bearing record.

The audit uses **coherent** to mean that accepted claims can be used together
without conflict, unrecorded dependencies, confusing ownership, provenance
drift, or movement across canon, working, proposal, story, belief, and design
boundaries. It does not require complete maps, distances, scientific models,
or species inventories.

## Corpus and coverage

### Canon authority map

Every canon content page was read in full. Domain `README.md` files were also
considered to confirm where still-empty subject areas are supposed to live.

| Subject | Authoritative owner | Canon level | Primary provenance | Dependencies and boundaries checked |
| --- | --- | --- | --- | --- |
| Highwall city and civilization | [`highwall.md`](../../canon/places/highwall.md) | established | Design A01, Highwall overview, regional geography, geology, hydrology, and climate reviews | Detailed geology, climate, hydrology, ecology, trade, government, story reveal, and working-name boundaries |
| Regional geology and geomorphology | [`highwall-region-geology.md`](../../canon/places/highwall-region-geology.md) | established | Geology S01 and hydrology A01 reviews | Plateau, basin, escarpments, canyon formation, lake chronology, hydrology |
| Regional climate | [`highwall-region-climate.md`](../../canon/places/highwall-region-climate.md) | established | Climate S01 review | Sea, escarpment, snowpack, storms, hydrology, ecology, human seasonal activity |
| Regional hydrology | [`highwall-region-hydrology.md`](../../canon/places/highwall-region-hydrology.md) | established | Hydrology S01/A01/A02 and climate S01 reviews | River identity, groundwater unknowns, three lakes, hidden basin, climate |
| Regional ecology | [`highwall-region-ecology.md`](../../canon/places/highwall-region-ecology.md) | established | Ecology S01 review | Physical drivers, broad niches, human management, working inventory |
| Regional flora and fauna | [`highwall-region-flora-and-fauna.md`](../../canon/places/highwall-region-flora-and-fauna.md) | working | Ecology S02 review | Established ecological niches, proposals, unresolved inventory, real-world analogues |
| Upriver Highlands | [`upriver-highlands.md`](../../canon/places/upriver-highlands.md) | established | Regional geography, geology, and hydrology reviews | Plateau, inland basin, clans, resources, trade |
| Stormlands | [`stormlands.md`](../../canon/places/stormlands.md) | established | Regional geography and climate reviews | Coastal plain, rain, forests, Delta river, trade, working organisms |
| Delta | [`delta.md`](../../canon/places/delta.md) | established | Regional geography S01 review | Agriculture, two water relationships, naval presence, trade |
| Forge | [`forge.md`](../../canon/places/forge.md) | established | Regional geography S01 review | Downstream status, manufacturing role, unestablished place type |
| Ledger | [`ledger.md`](../../canon/places/ledger.md) | established | Regional geography S01 review | Noncontiguous identity, ports, finance, currency exchange |
| Regional trade | [`regional-trade-system.md`](../../canon/economy/regional-trade-system.md) | established | Regional geography S01/A01 reviews | Place specializations, corridor, currency, imperial obligations |
| Regional government | [`regional-imperial-structure.md`](../../canon/government/regional-imperial-structure.md) | established | Regional geography A01 review | Internal sovereignty, imperial classification, official terminology, story reveal |

The remaining canon domains contain navigation and ownership rules but no
setting content pages. Their empty state was checked against exclusions and
open dependencies; no absent page was treated as evidence that a fact is
false.

### Boundary and lifecycle corpus

- Read [`Highwall Design Principles`](../../design/principles.md) and both
  design navigation/boundary documents.
- Read the complete `story/` tree, including the
  [`Regional Imperial Relationship Reveal`](../../story/reveals/regional-imperial-relationship.md)
  and the empty project, chronology, and character-knowledge indexes.
- Read all twelve open-question records, both proposals, the one contradiction
  report, the empty decision and retired indexes, and the complete
  [`canon change log`](../canon-changes.md).
- Checked resolution state, affected-page text, links, and present-corpus
  constraints for all fifteen substantive development exception records.

### Provenance and claim coverage

All 26 intake reviews were read. The generated
[`claim index`](../indexes/claim-index.json) contains 261 claims, and all 261
were included in the coverage pass. The index was also compared with its
generator and source review tables rather than treated as authority.

| Case | Reviews read | Indexed claims |
| --- | ---: | ---: |
| `CASE-2026-08-03-GITHUB-MERGE-POLICY` | 3 | 11 |
| `CASE-2026-08-03-REPOSITORY-FOUNDATION` | 5 | 21 |
| `CASE-2026-08-04-AUTHORIAL-DESIGN-PRINCIPLES` | 2 | 13 |
| `CASE-2026-08-04-HIGHWALL-OVERVIEW` | 1 | 26 |
| `CASE-2026-08-04-INTAKE-COMPLETENESS-GITHUB-APPROVALS` | 1 | 3 |
| `CASE-2026-08-04-LORE-SEED-BOUNDARIES` | 1 | 7 |
| `CASE-2026-08-04-LORE-SEED-TEMPLATE` | 2 | 6 |
| `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY` | 3 | 48 |
| `CASE-2026-08-05-GEOLOGY-GEOMORPHOLOGY` | 1 | 29 |
| `CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW` | 1 | 8 |
| `CASE-2026-08-06-REGIONAL-CLIMATE` | 1 | 25 |
| `CASE-2026-08-06-REGIONAL-HYDROLOGY` | 3 | 29 |
| `CASE-2026-08-07-REGIONAL-ECOLOGY` | 2 | 35 |
| **Total** | **26** | **261** |

The disposition totals were 122 `create`, 78 `update`, 36 `no-change`, 19
`defer`, 3 `out-of-scope`, 2 `link-only`, and 1 `conflict`. The seven
setting/design cases account for 205 claims; the six process cases account for
56 claims and were included to test repository and authority boundaries.

Immutable submissions were used only where a review or index summary could
not settle a candidate. Exact source passages were checked in the Highwall
overview, geology, climate, and both ecology submissions. Hydrology A01/A02
review evidence was sufficient for the resolved lake and Old Wall chronology.

## Audit method

1. **Inventory and authority map:** Identified the single expected owner,
   canon level, provenance, dependencies, and story/design boundary for each
   regional subject before assessing repeated prose.
2. **Physical causality:** Traced geology through landform, climate,
   hydrology, ecological zones, working niches, and human water and land use.
3. **Spatial geography:** Compared all relative positions, elevations,
   upstream/downstream statements, waterways, basins, escarpments, corridors,
   jurisdictions, and uses of Highwall.
4. **Human systems:** Traced water, land, flood, and seasonal facts into
   settlement, agriculture, trade, labor, autonomy, and imperial obligations.
5. **Authority and duplication:** Compared every repeated substantive regional
   fact with its detailed owner, contextual summary, links, and provenance.
6. **Terminology and identity:** Checked Highwall, Dryrun, unnamed rivers,
   inland/hidden/Salt Basin, three lake referents, Stormlands/coast, rock names,
   and real-world analogues.
7. **Authority boundaries:** Compared established, working, proposal, open
   question, belief, history, story reveal, and design material.
8. **Provenance verification:** Checked each candidate against exact claim
   rows, dispositions, targets, source passages where necessary, addenda,
   corrections, and later claims.
9. **Development lifecycle:** Checked present accuracy and linkage of open,
   resolved, proposed, contradicted, and change-log records without
   restructuring them.

Scientific plausibility was used only to notice possible dependencies. No
external scientific model or inferred mechanism was used as setting evidence.

## Findings

### `T3-2026-08-07-F01` — Canyon origin remains contradictory in the accepted claim set

- **Category and severity:** Contradiction — **Critical**
- **Exact pages and sections:**
  [`Highwall Overview Seed Review` — `Claim decisions`](../intake-reviews/2026-08-04-highwall-overview-s01-review.md),
  [`Geology and Geomorphology Seed Review` — `Files inspected`, `Claim decisions`, and `Conversation checkpoint`](../intake-reviews/2026-08-05-geology-geomorphology-s01-review.md),
  [`Highwall` — `Geography and environment`](../../canon/places/highwall.md),
  [`Regional Geology` — `Highwall canyon`](../../canon/places/highwall-region-geology.md),
  and the corresponding rows in the
  [`claim index`](../indexes/claim-index.json).
- **Related claim IDs:**
  `CASE-2026-08-04-HIGHWALL-OVERVIEW-S01-C002`;
  `CASE-2026-08-05-GEOLOGY-GEOMORPHOLOGY-S01-C020`, `C021`, and `C023`.
- **Neutral description:** The accepted Highwall review says the intermittent
  river formed the canyon. The later geology review establishes that the
  ancient lake-drainage megaflood excavated essentially the entire canyon and
  that the modern intermittent river inherited rather than formed it. The
  geology review repeatedly calls this a correction, but all three geology
  rows record `Supersedes: None`; the older claim therefore remains an
  accepted `update` claim in the generated claim set.
- **Why the passages do or do not coexist:** “The modern intermittent river
  formed the canyon” and “the canyon formed by megaflood rather than the modern
  river” cannot both stand as objective formation accounts. Current canon prose
  consistently uses the later megaflood model, so the contradiction is in
  accepted claim provenance rather than between current canon pages.
- **Downstream impact:** A future intake or story audit routed through the
  claim index can recover the earlier formation claim as still accepted and
  reintroduce incompatible geology, river history, or flood terminology.
- **Permissible next action:** Open a separate authorized provenance and
  supersession case. Preserve both source claims, obtain any needed authorial
  clarification, and then record the authoritative relationship before
  changing reviews, canon, or the generated index.
- **Explicitly prohibited inference:** This audit does not decide that recency
  silently invalidates C002, declare the geology source an implicit addendum to
  the Highwall case, or edit either authority.
- **Verification performed:** Compared both immutable source passages, all
  four review rows including their `Supersedes` cells and rationales, the
  generated index entries, current Highwall and geology prose, the river-name
  question, and the canon change log. No correction addendum or supersession
  record resolves the accepted-claim conflict.

### `T3-2026-08-07-F02` — Climate prose crosses its agriculture and working-organism boundary

- **Category and severity:** Boundary leak — **Material**
- **Exact pages and sections:**
  [`Regional Climate Seed` — `Culture, systems, and terminology` and `Explicit exclusions`](../../intake/submissions/2026-08-06-regional-climate-s01.md),
  [`Regional Climate Seed Review` — claims C018 and C025](../intake-reviews/2026-08-06-regional-climate-s01-review.md),
  [`Regional Climate` — `Storm season and regional life`](../../canon/places/highwall-region-climate.md),
  [`Regional Flora and Fauna` — `Status and scope`, `Basin inventory`, and `Human-influenced organisms`](../../canon/places/highwall-region-flora-and-fauna.md),
  and the [canon change log's ecology entry](../canon-changes.md).
- **Related claim IDs:**
  `CASE-2026-08-06-REGIONAL-CLIMATE-S01-C018` and `C025`;
  `CASE-2026-08-07-REGIONAL-ECOLOGY-S02-C006`, `C009`, and `C010`.
- **Neutral description:** Climate C018 establishes that storm season affects
  “Blueleaf harvests” and “reed cultivation” on an established canon page.
  The same climate seed explicitly says it does not establish agriculture,
  and no earlier accepted authority establishes either named activity. The
  later ecology case keeps reeds and their managed-wetland use on a working
  page and states that named organisms in that inventory remain working.
- **Why the passages do or do not coexist:** A climate dependency can be
  stated without owning an industry's detailed practice, but naming harvest
  and cultivation activities on an established page necessarily reads as
  evidence that those activities exist. That reading exceeds the seed's
  agriculture exclusion and makes the authority of reeds differ between the
  established climate page and the working inventory. Blueleaf has no other
  authority at all.
- **Downstream impact:** Agriculture, economy, organism, or seasonal-labor work
  may cite the climate page to treat Blueleaf or reeds as established despite
  the later working boundary.
- **Permissible next action:** Use a separate authorized claim-to-canon
  boundary case to clarify the intended authority of C018 and then align the
  climate review, canon wording, working inventory, and change-log description
  as authorized.
- **Explicitly prohibited inference:** Do not infer what Blueleaf is, infer a
  crop or species, establish cultivation mechanics, promote reeds, or choose
  whether C018 should remain established.
- **Verification performed:** Searched the complete corpus for both terms,
  inspected the exact climate source and exclusions, checked C018's evidence
  and disposition, checked all later ecology claims and page levels, and found
  no prior agriculture or organism authority that supplies the missing premise.

### `T3-2026-08-07-F03` — “Salt Basin” has no established identity relationship

- **Category and severity:** Terminology ambiguity — **Material**
- **Exact pages and sections:**
  [`Regional Climate` — `Climatic zones`](../../canon/places/highwall-region-climate.md),
  [`Regional Geology` — `Inland basin`](../../canon/places/highwall-region-geology.md),
  [`Regional Hydrology` — `Inland collapsed-lake basin` and `Hidden basin`](../../canon/places/highwall-region-hydrology.md),
  and [`Regional Ecology` — `Inland basin`](../../canon/places/highwall-region-ecology.md).
- **Related claim IDs:**
  `CASE-2026-08-06-REGIONAL-CLIMATE-S01-C012`;
  `CASE-2026-08-05-GEOLOGY-GEOMORPHOLOGY-S01-C012`, `C015`, and `C016`;
  `CASE-2026-08-06-REGIONAL-HYDROLOGY-S01-C015` through `C019`;
  `CASE-2026-08-07-REGIONAL-ECOLOGY-S01-C008`.
- **Neutral description:** Climate alone names a “Salt Basin.” Geology and
  hydrology name an inland basin with salt flats, marginal fresh water, and a
  smaller saline lake; ecology uses “inland basin” or generic “basin.” A
  separate hidden basin is explicitly established. No canon statement,
  front-matter alias, review disposition, or open question says whether Salt
  Basin and inland basin are the same referent.
- **Why the passages do or do not coexist:** Their physical descriptions make
  shared identity plausible, and the climate review uses hydrology as evidence
  for C012, but similarity and reviewer context cannot establish an alias. If
  they are distinct, the pages do not locate both; if they are identical, the
  authority map lacks that identity relationship. The hidden basin is clearly
  distinct and does not resolve the other two names.
- **Downstream impact:** Climate, hydrology, ecology, travel, and settlement
  work can attach wetlands, lakes, or communities to the wrong basin.
- **Permissible next action:** Request an authorial terminology clarification
  in a separate case, then record either the alias or the distinction in the
  appropriate authority and metadata.
- **Explicitly prohibited inference:** Do not equate Salt Basin with inland
  basin from matching salt-flat descriptions, and do not merge either with the
  hidden basin.
- **Verification performed:** Searched canon, reviews, claim index,
  development records, and relevant submissions for every basin term. The
  climate source is the sole source of “Salt Basin”; no identity or alias
  claim was found.

### `T3-2026-08-07-F04` — Claim-index rows do not surface working authority

- **Category and severity:** Linkage gap — **Material**
- **Exact pages and sections:**
  [`claim-index.json`](../indexes/claim-index.json),
  [`Regional Flora and Fauna Seed Review` — front matter and `Claim decisions`](../intake-reviews/2026-08-07-regional-ecology-s02-review.md),
  [`Regional Flora and Fauna` — front matter and `Status and scope`](../../canon/places/highwall-region-flora-and-fauna.md),
  and [`Consistency Workflow` — `Claim index`](../../references/consistency-workflow.md).
- **Related claim IDs:**
  `CASE-2026-08-05-SCALABLE-CONSISTENCY-WORKFLOW-S01-C003` and
  `CASE-2026-08-07-REGIONAL-ECOLOGY-S02-C001` through `C018`.
- **Neutral description:** The index correctly labels itself
  `navigation-only`, but individual claim rows do not include the review's
  `authority: working-canon` or the target page's `canon_level: working`.
  Ecology S02 rows C001-C013 instead display `classification: canon`,
  `authority_basis: explicit`, and `create`/`update`; only row prose and the
  linked review/page reveal that these are working claims.
- **Why the passages do or do not coexist:** The navigation-only disclaimer
  prevents the index from becoming canon, so the index does not itself promote
  organisms. It nevertheless fails to carry the authority attribute needed to
  distinguish established from working canon during claim discovery. The gap
  is material because the index is the prescribed route to earlier claims.
- **Downstream impact:** Automated or hurried intake can treat working rows as
  established before following the review, increasing accidental promotion
  risk across every future mixed-authority case.
- **Permissible next action:** In a separate authorized tooling task, evaluate
  adding review authority or target canon level to the generated schema and
  context output, with validation tests and without changing any claim's
  actual authority.
- **Explicitly prohibited inference:** Do not treat the index as authoritative,
  reinterpret `classification: canon` as `canon_level: established`, or change
  the S02 review/page level during this audit.
- **Verification performed:** Compared all S02 index rows with the review
  front matter, working page front matter, generator fields, index policy, and
  established S01 rows. The generator does not emit per-review authority or
  target canon level.

### `T3-2026-08-07-F05` — Highwall's central relationship metadata is empty

- **Category and severity:** Linkage gap — **Material**
- **Exact pages and sections:**
  [`Highwall` — front matter, `Economy and infrastructure`, and `Open issues`](../../canon/places/highwall.md),
  plus the front matter of the regional
  [geology](../../canon/places/highwall-region-geology.md),
  [climate](../../canon/places/highwall-region-climate.md),
  [hydrology](../../canon/places/highwall-region-hydrology.md),
  [ecology](../../canon/places/highwall-region-ecology.md),
  [working inventory](../../canon/places/highwall-region-flora-and-fauna.md),
  [trade](../../canon/economy/regional-trade-system.md), and
  [government](../../canon/government/regional-imperial-structure.md) pages.
- **Related claim IDs:**
  `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-S01-C005` and `C006`;
  `CASE-2026-08-05-GEOLOGY-GEOMORPHOLOGY-S01-C020` and `C021`;
  `CASE-2026-08-06-REGIONAL-CLIMATE-S01-C008` and `C020`;
  `CASE-2026-08-06-REGIONAL-HYDROLOGY-S01-C010`;
  `CASE-2026-08-07-REGIONAL-ECOLOGY-S01-C017`.
- **Neutral description:** Highwall is the central subject and its body links
  geology, hydrology, climate, and trade, while seven specialized authorities
  link back to it. Its front matter nevertheless remains `related: []`, and
  the body does not surface the government, ecology, or working-inventory
  relationships.
- **Why the passages do or do not coexist:** Body links keep several paths
  navigable and no factual contradiction results. The empty metadata is still
  misleading as an authority map because it says the central page has no
  directly related authorities while backlinks show the opposite.
- **Downstream impact:** Targeted discovery beginning at Highwall can omit
  high-risk political, ecological, or working-canon context and encourage new
  duplication on the overview page.
- **Permissible next action:** Perform a separate audit-only relationship and
  ownership maintenance pass that selects a restrained set of reciprocal
  metadata/body links without copying substantive explanations.
- **Explicitly prohibited inference:** Do not make every backlink reciprocal,
  treat `related` as exhaustive taxonomy, or move specialized facts back into
  Highwall.
- **Verification performed:** Compared Highwall's front matter and body links
  with all canon `related` lists and backlinks. Highwall is the only content
  page with an empty relationship list.

### `T3-2026-08-07-F06` — Two human-readable source sections omit valid climate provenance

- **Category and severity:** Linkage gap — **Minor**
- **Exact pages and sections:**
  [`Regional Hydrology` — front matter and `Sources and decisions`](../../canon/places/highwall-region-hydrology.md)
  and [`Stormlands` — front matter and `Sources and decisions`](../../canon/places/stormlands.md).
- **Related claim IDs:**
  `CASE-2026-08-06-REGIONAL-CLIMATE-S01-C003`, `C007`, `C009`, `C014`, and
  `C020`.
- **Neutral description:** Both pages correctly include the climate review in
  front-matter provenance after climate materially refined their prose, but
  their human-readable `Sources and decisions` lists omit that same review.
- **Why the passages do or do not coexist:** Machine-readable provenance is
  correct, so no claim lacks source authority. The duplicated human-readable
  source surface is incomplete and can mislead a reader who uses only the end
  section.
- **Downstream impact:** Manual provenance review takes an avoidable detour and
  may miss the climate-to-hydrology or climate-to-Stormlands change history.
- **Permissible next action:** Add the missing review links in a separate
  process-only editorial maintenance task, ideally alongside an ownership pass.
- **Explicitly prohibited inference:** Do not remove the valid front-matter
  provenance or infer that the climate changes were unreviewed.
- **Verification performed:** Compared every canon page's front-matter
  provenance with its `Sources and decisions` links and checked the climate
  review's changed-file and claim tables.

### `T3-2026-08-07-F07` — Resolved sovereignty record still points to a future authority

- **Category and severity:** Stale development record — **Minor**
- **Exact pages and sections:**
  [`Completion of the regional sovereignty statement` — front matter,
  `Affected pages`, and `Resolution`](../open-questions/regional-sovereignty-source-completion.md)
  and [`Regional Imperial Structure` — `Objective structure`](../../canon/government/regional-imperial-structure.md).
- **Related claim IDs:**
  `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-S01-C028` and
  `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-A01-C001`.
- **Neutral description:** The question is correctly marked resolved and its
  resolution links the completing addendum and review, but `Affected pages`
  still says “Future regional government documentation” and `related` omits
  the now-existing government authority.
- **Why the passages do or do not coexist:** The resolution and current canon
  agree on internal sovereignty. Only the lifecycle/navigation description
  remains frozen at the pre-resolution state.
- **Downstream impact:** A lifecycle audit may not discover the authoritative
  result directly from metadata, and the affected-page list inaccurately
  describes the current repository.
- **Permissible next action:** Update only the resolved record's links and
  affected-page reference in a separate routine maintenance task.
- **Explicitly prohibited inference:** Do not reinterpret sovereignty, alter
  imperial relationships, or reopen the resolved source-completion question.
- **Verification performed:** Compared the incomplete S01 claim, completing
  A01 claim, resolved question, government page, review links, and claim-index
  entries.

## Verified coherent relationships

These negative results are retained because they cover relationships most
likely to be misread or to regress.

### `T3-2026-08-07-V01` — Physical causality chain

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Regional geology `Geological structure` through
  `Highwall canyon`; climate C001-C017; hydrology C001-C015 and C021; ecology
  C001-C013.
- **Why the passages coexist:** Resistant caprock, plateau and escarpments,
  canyon incision, coastal rain shadow, mountain snow, storm season, seasonal
  river behavior, wetlands, and ecological zones form a continuous chain. The
  pages state broad consequences while leaving aquifer architecture,
  discharge, climate values, and community boundaries open.
- **Downstream impact:** Later environment or settlement work can rely on the
  broad chain but must preserve its open mechanisms.
- **Permissible next action:** Continue using the specialized pages as owners
  and their open questions for missing detail.
- **Explicitly prohibited inference:** Do not derive aquifer layers,
  watershed maps, rainfall values, or species from plausibility.
- **Verification performed:** Compared all six regional environmental pages,
  their provenance, linked questions/proposals, and the relevant 118 climate,
  hydrology, geology, and ecology case claims.

### `T3-2026-08-07-V02` — Lake and flood chronology

- **Category and severity:** Verified coherent — **Critical relationship**
- **Pages and claims:** Geology C015-C021; hydrology S01 C006, C016, and C021;
  hydrology A01 C001-C003; hydrology A02 C001; the
  [resolved standing-water contradiction](../contradictions/inland-basin-standing-water.md).
- **Why the passages coexist:** The corpus distinguishes (1) the ancient
  basin-filling lake and millennia-old canyon-forming megaflood, (2) the much
  smaller present saline lake with roughly decadal overflow, (3) the
  canyon-entrance lake whose collapse caused the Old Wall flood about 185 years
  ago, and (4) ordinary and exceptional seasonal flash floods.
- **Downstream impact:** History and story work can keep the four event classes
  separate.
- **Permissible next action:** Preserve the established distinctions and route
  detailed mechanics or dates to existing open questions.
- **Explicitly prohibited inference:** Do not make a present-lake overflow an
  Old Wall event or equate an ordinary flood with either catastrophic lake
  drainage.
- **Verification performed:** Checked the original conflict disposition,
  A01/A02 corrections, both authority pages, Highwall history, change log, and
  resolved contradiction status.

### `T3-2026-08-07-V03` — Seasonal climate and hydrology

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Climate C002-C007 and C011-C017; hydrology C001-C014
  and C021.
- **Why the passages coexist:** Western winter moisture, eastern mountain
  snowpack, spring snowmelt, late-summer tropical moisture, localized upstream
  storms, drought, and Highwall flooding use the same seasons and sources.
  Climate owns atmospheric distribution; hydrology owns water response.
- **Downstream impact:** Seasonal labor, travel, flood preparedness, and water
  availability have a stable calendar at broad resolution.
- **Permissible next action:** Add quantitative or local detail only with new
  authority.
- **Explicitly prohibited inference:** Do not infer rainfall totals, exact
  storm-belt boundaries, or an annual hydrograph.
- **Verification performed:** Traced every seasonal statement in the climate,
  hydrology, Highwall, and open-question records.

### `T3-2026-08-07-V04` — Regional river identities remain safely distinct

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Regional geography S01 C023-C024; A01 C013; hydrology
  C004-C007; the [regional river-name question](../open-questions/regional-river-names.md).
- **Why the passages coexist:** Working-name Dryrun is intermittent and joins
  a larger permanent river near its mouth. A river originating in the
  Stormlands supplies most Delta water. Delta also receives Highwall flood
  pulses. The corpus explicitly prohibits assuming that the named river
  references are the same and does not need that identity to state the two
  Delta water relationships.
- **Downstream impact:** Maps and travel work can preserve the relationships
  without inventing a confluence or river name.
- **Permissible next action:** Await river naming and mapping authority.
- **Explicitly prohibited inference:** Do not identify Dryrun, the larger
  perennial river, and the Stormlands-Delta river with one another.
- **Verification performed:** Compared all waterway canon, both naming
  questions, geography and hydrology reviews, and matching index claims.

### `T3-2026-08-07-V05` — Working organism inventory is otherwise contained

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Ecology S01 C001-C017; ecology S02 C001-C018; the
  established ecology page, working flora/fauna page, organism proposal, and
  both ecology detail questions.
- **Why the passages coexist:** The ecology page establishes zones, functions,
  disturbance, and broad human influence without selecting species. The
  inventory states `canon_level: working`, calls itself provisional, links
  unapproved fictionalization separately, and keeps detailed inventory open.
  Named species-level roles remain on the working page. F02 is the bounded
  exception involving earlier climate prose.
- **Downstream impact:** Later organism design can revise names and occupants
  without changing the established niche structure.
- **Permissible next action:** Continue to require explicit promotion
  authority for any organism.
- **Explicitly prohibited inference:** Do not cite page location under
  `canon/` as evidence of established level or treat analogues as fictional
  canonical identities.
- **Verification performed:** Checked front matter, status prose, every S02
  disposition, links to questions/proposals, change-log notes, and all named
  organism occurrences.

### `T3-2026-08-07-V06` — Sovereignty, official language, and reader reveal

- **Category and severity:** Verified coherent — **Critical relationship**
- **Pages and claims:** Regional geography A01 C001-C011; Highwall overview
  C021-C022; regional government `Objective structure` and `Official regional
  position`; story reveal in full.
- **Why the passages coexist:** Polities are internally sovereign while the
  region objectively functions as an imperial tributary province. Official
  regional language emphasizes diplomacy and shared obligations, and the
  story page controls when readers learn the difference. Character knowledge
  remains unestablished.
- **Downstream impact:** Political and narrative work can preserve both
  objective structure and early-story obscurity without treating official
  language as a contradiction.
- **Permissible next action:** Route new objective politics to government and
  reveal timing or viewpoint knowledge to story.
- **Explicitly prohibited inference:** Do not infer what any character knows
  or convert official terminology into objective independence from the empire.
- **Verification performed:** Compared source classifications, belief/story
  dispositions, government and story pages, Highwall's attributed history,
  and all relevant backlinks.

### `T3-2026-08-07-V07` — Trade dependencies and political obligations

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Regional geography S01 C001-C027; A01 C003-C006;
  Highwall `Economy and infrastructure`; all five regional place pages;
  regional trade and government pages.
- **Why the passages coexist:** Each place owns its identity and local facts,
  the trade page owns specialization and exchange, and government owns
  imperial authority. Highwall's surrounding highlands can supply scarce
  materials while the Stormlands remain the region's largest timber and ore
  supplier; no exclusivity claim conflicts.
- **Downstream impact:** Economy and settlement work have a coherent dependency
  network without requiring distances, volumes, or a complete regional list.
- **Permissible next action:** Preserve linked summaries and await specific
  production, scale, and travel authority.
- **Explicitly prohibited inference:** Do not derive route distances, trade
  shares, Forge's place type, or exhaustive political geography.
- **Verification performed:** Compared every economic claim with place-level
  summaries, provenance, excluded detail, government obligations, and open
  geography questions.

### `T3-2026-08-07-V08` — Most repeated authority is contextual rather than competing

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Highwall and regional trade summaries; Stormlands and
  climate forest/rain relationship; economy and government obligations;
  ecology and physical-driver links; working-page wildfire context.
- **Why the passages coexist:** Detailed explanations stay on specialized
  authorities. Other pages repeat only the local consequence or enough context
  to navigate, usually with a direct body or metadata link. The government and
  economy pages explicitly distinguish political authority from economic
  consequence. F05 and F06 identify the bounded link defects.
- **Downstream impact:** The present ownership model can scale if new work
  follows the same summary-plus-link pattern.
- **Permissible next action:** Use an ownership pass for the bounded navigation
  defects rather than rewriting the full regional corpus.
- **Explicitly prohibited inference:** Do not remove useful local summaries or
  treat every repeated phrase as competing authority.
- **Verification performed:** Compared each repeated substantive claim with
  review targets, changed-file rationales, page links, and authority level.

### `T3-2026-08-07-V09` — Working names and real-world analogues stay qualified

- **Category and severity:** Verified coherent — **Material relationship**
- **Pages and claims:** Hydrology C004; Highwall and hydrology Dryrun prose;
  river-name question; ecology S02 C001, C007, C016; organism proposal; design
  and repository boundary rules.
- **Why the passages coexist:** Dryrun is always identified as a working
  development name, and no final river name is implied. Mesquite-like,
  raccoon-like, and redwood-analogue organisms remain working comparisons;
  fictionalization and renaming remain proposals.
- **Downstream impact:** Contributors can use stable development labels without
  converting them into final terminology or fictional taxonomy.
- **Permissible next action:** Keep qualifiers until explicit naming or
  promotion authority arrives.
- **Explicitly prohibited inference:** Do not create aliases, species, or
  in-world real-world identities from the working labels.
- **Verification performed:** Searched the complete corpus for every working
  name and analogue and checked page level, proposal state, and claim
  disposition.

## Deliberate non-findings

- The ancient basin lake, present saline lake, and Old Wall lake are not a
  remaining contradiction; hydrology A01/A02 and the resolved contradiction
  record distinguish them.
- Ordinary flash floods, occasional exceptional floods, the Old Wall flood,
  and the ancient megaflood are not conflated in current canon.
- The intermittent Highwall river, its larger perennial receiving river, and
  the Stormlands-Delta river were not assumed to be one river.
- “Only practical corridor” is compatible with possible alternatives whose
  use is negligible; A02 explicitly establishes both parts.
- Internal sovereignty and imperial tributary status are not a contradiction
  because the scope and perspective distinctions are explicit.
- Highwall's and the Stormlands' timber and ore statements are not a conflict:
  one establishes a local source and the other the largest regional supplier.
- Hidden-basin agriculture is not treated as a scientifically filled gap. The
  bounded water capacity is established while the retention mechanism remains
  open.
- The two ecology questions have overlapping inventory context but distinct
  broad-community and organism-detail scopes, with an explicit cross-link; no
  stale resolution was found.
- Publication fields in older completed reviews were not treated as stale.
  Current policy deliberately leaves publication state in GitHub rather than
  adding audit-only updates to completed reviews.
- Missing distances, maps, coordinates, climate values, discharge, aquifer
  structure, and detailed species are deliberate unknowns, not contradictions
  or invitations to scientific inference.
- No new contradiction report was created. F01 requires a separate authorized
  successor case under the stated audit boundary.

## Coverage limitations

- The regional map listed in the regional geography A01 source was not
  available to its original review and is not present in the repository. This
  audit therefore tested textual relative geography only.
- Exact distances, travel times, coordinates, watershed maps, and climatic or
  hydrologic quantities are explicitly unestablished. The audit cannot verify
  cartographic or quantitative consistency that the corpus does not claim.
- Immutable submissions were consulted only for candidate findings whose
  review summaries were insufficient. The complete submission corpus was not
  treated as an independent authority layer.
- No external scientific research was used. Scientific plausibility did not
  replace repository evidence.
- F02 identifies an authority-boundary defect, but the intended authorial
  resolution of the climate statement cannot be inferred. F03 likewise cannot
  establish basin identity. Additional reasoning would not replace the missing
  authority, so no max follow-up pass is recommended.
- Draft PR creation and GitHub checks occur after the report-only commit and
  push. Their eventual state belongs in GitHub and the completion report, not a
  follow-up audit-only edit.

## Recommended successor tasks

1. **Canyon-origin claim provenance and supersession case.** Highest
   continuity risk: it is the only direct incompatible accepted-claim pair,
   affects geology, hydrology, history, terminology, and story continuity, and
   currently lacks an authorized supersession record. This task should decide
   only the provenance relationship with explicit author authority and should
   not invent new geology.
2. **Climate boundary and basin-identity clarification case.** Resolve F02 and
   F03 through narrow authorial clarification: determine the intended authority
   of Blueleaf/reed activity and whether Salt Basin is an alias for the inland
   basin or a distinct referent. Both issues originate in the climate case and
   affect several downstream environmental and human-system pages.
3. **Authority-discovery and ownership maintenance.** A process/tooling task
   addressing F04-F07: surface working authority in generated claim discovery,
   curate Highwall's central relationships, align human-readable source links,
   and refresh the resolved sovereignty record. It requires no new lore and
   can reduce recurrence at comparatively low effort; any claim-index schema
   change still needs explicit process authority.

These rankings prioritize continuity risk, downstream reach, work possible
without new lore, recurrence prevention, and value relative to effort. They
favor claim-to-canon provenance remediation before a broader duplication
rewrite.

## Retrospective

The current canon pages present a substantially coherent regional model. The
physical chain, seasonal water cycle, ecology structure, trade system, and
political/story layers can be used together without filling scientific gaps.
The audit found one critical contradiction confined to accepted claim
provenance, four material authority/terminology/linkage defects, and two minor
navigation/lifecycle defects. It also preserved nine high-risk coherent
relationships.

The most important pattern is not scientific inconsistency but authority
discoverability: later pages often contain the correct present model while an
older accepted claim, an exclusion boundary, a missing identity link, or a
generated navigation row leaves a competing path for future intake. The
recommended work therefore begins with provenance and boundary clarification,
then uses tooling and metadata to reduce recurrence.

No canon, story, design, submission, intake review, claim index, proposal,
question, contradiction, decision, or policy file was changed. No claim was
promoted, answered, retired, or re-disposed.

## Validation and publication status

- [x] Repository validation passes against `origin/main`.
- [x] Generated claim index is current.
- [x] `git diff --check` passes.
- [x] Complete diff contains only this maintenance report.
- [x] No setting, story, belief, historical, or design claim was introduced.
- [x] No authority or contradiction decision was made.
- [x] Every canon content page and every intake review was considered.
- [x] Every candidate finding was checked against provenance.
- [ ] Draft pull request opened.
- [ ] `Canon and intake integrity` passes on GitHub.
- [ ] `Markdown style` passes on GitHub.

**Publication:** Pending. GitHub check history and the eventual commit/PR state
will be reported externally and will not be copied into this report through an
audit-only follow-up commit.
