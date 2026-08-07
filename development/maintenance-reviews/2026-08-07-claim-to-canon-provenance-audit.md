# Maintenance Review: Claim-to-Canon Provenance Audit

## Scope and authority boundary

- **Audit ID:** `MAINT-2026-08-07-CLAIM-TO-CANON-PROVENANCE-AUDIT`
- **Objective:** Establish bidirectional traceability between the complete
  reviewed claim set and every substantive passage in current canon.
- **Authority:** Audit-only routine maintenance. This report records evidence,
  findings, verified relationships, and successor recommendations; it grants
  no lore, story, design, or repository-policy authority.
- **Session mode:** Direct audit of accepted repository state. No intake case,
  submission, addendum, claim disposition, or authority change was created.
- **Branch:** `agent/claim-to-canon-provenance-audit`
- **Permitted change:** This maintenance report only.

The audit may identify missing or ambiguous provenance, incomplete or excess
implementation, target or disposition drift, supersession gaps, authority
level mismatches, duplicate implementation, exceptional-disposition gaps, and
linkage defects. It does not repair any finding, reinterpret a source, decide
an unresolved issue, change canon, rewrite a historical review, or treat
reviewer inference as authorial authority.

For this report, a passage is **traceable** when its substantive assertions are
bounded by one or more reviewed claims with sufficient authorial authority,
the current disposition and target remain intelligible, later corrections are
visible, and page-level provenance identifies every review that materially
established or changed the passage. Headings, connective prose, navigation,
and organizational wording that add no substantive assertion do not require a
separate claim ID.

## Audit baseline

- **Audited commit:**
  `027d0e36b8c20689b3d9fa0473f1860907720919` (`Improve authority discovery
  and ownership links (#19)`).
- **Previous Tier 3 baseline:**
  `723d457928ee357ad51e164340e1e7252bac9f30` (`Record regional Tier 3
  semantic audit`).
- **Canyon-origin successor:**
  `fc5d352f48f99d1e3bca110561fc66ad3151fc7f` (PR #17).
- **Climate-boundary and Salt Basin successor:**
  `1b404bae63ba8c05944bf1f11d9d8550b7737dcf` (PR #18).
- **Authority-discovery and ownership successor:**
  `027d0e36b8c20689b3d9fa0473f1860907720919` (PR #19).
- **Repository state:** `main` was clean, matched `origin/main`, and was
  explicitly fast-forward synchronized before the unused branch name was
  created. No local branch, remote branch, or earlier PR used the requested
  name.

The baseline is the exact accepted state against which a later incremental
audit can inspect Git history. Unchanged files are not automatically carried
forward: each verified relationship below states the semantic changes that
invalidate it.

## Corpus and coverage

### Complete corpus considered

- All **13** substantive canon pages under `canon/`. Navigational `README.md`
  files were checked only for domain ownership and scope.
- All **28** intake reviews under `development/intake-reviews/`, containing
  **264** indexed claims across 13 cases.
- The generated claim index at schema version 2, used as navigation and
  compared with the source review tables.
- All relevant immutable submissions where a review summary could not settle
  exact scope. Exact source text was checked for Highwall corridor traffic,
  Forge location, canyon origin, climate activities, Salt Basin identity,
  inland-lake chronology, hidden-basin access, sovereignty, ecology, and
  working organism claims.
- The complete canon change log; both contradiction reports; all 12 open
  questions; both proposals; the empty decision and retired-record indexes;
  the substantive story reveal; the design principles; and the previous Tier
  3 and authority-discovery maintenance reviews.

### Claim-set totals

| Review authority | Claims |
| --- | ---: |
| `establish-canon` | 177 |
| `working-canon` | 18 |
| `establish-policy` | 44 |
| `proposal-only` | 8 |
| `classify` | 17 |
| **Total** | **264** |

The seven setting/design cases plus the two later clarification claims account
for 208 claims. The six process cases account for 56 claims and were also
checked so that an administrative claim could not be mistaken for lore
authority.

| Disposition | Claims | Reconciliation result |
| --- | ---: | --- |
| `create` | 122 | Expected pages and records checked; one current canon assertion exceeds its reviewed claims (F02). |
| `update` | 81 | Expected effects checked; one compound claim is not fully represented (F01). |
| `link-only` | 2 | Climate-hydrology and ecology-physical-authority links exist in both directions. |
| `no-change` | 36 | Non-actions remain intelligible; one working page duplicates a fact that its review explicitly left at the established owner (F04). |
| `defer` | 19 | Required open-question or proposal records exist; current canon does not settle them. |
| `conflict` | 1 | Required contradiction record exists and its later authorized resolution is correct; index lifecycle discovery remains incomplete (F03). |
| `out-of-scope` | 3 | No unexplained canon or story implementation was found. |
| **Total** | **264** | Every indexed row was reconciled to its source review and present repository effect. |

### Canon pages included

| Page | Level | Substantive sections inspected | Principal supporting reviews and claims | Result |
| --- | --- | --- | --- | --- |
| [`highwall.md`](../../canon/places/highwall.md) | established | Summary; classification; geography; population; government; economy; culture; history | Design A01 C002-C005; Highwall S01 C001-C022 and A01 C001; geography S01 C002-C006 and A02 C001-C002; geology C020-C023; hydrology S01 C004-C006/C013 and A02 C001; climate C008/C013 | Provenance metadata is cumulative and authority is correct. Canyon-origin and overview synthesis are traceable. C005 is incompletely represented (F01). |
| [`highwall-region-geology.md`](../../canon/places/highwall-region-geology.md) | established | Structure; formations; plateau; inland basin; canyon | Geology C001-C023; hydrology A01 C001-C002; climate A01 C002 | Traceable, including Salt Basin identity and lake/canyon chronology. |
| [`highwall-region-climate.md`](../../canon/places/highwall-region-climate.md) | established | Regional pattern; zones; annual cycle; regional life; microclimates; water relationship | Climate S01 C001-C020 and A01 C001-C002 | Traceable. Established activities remain distinct from working biological detail. |
| [`highwall-region-hydrology.md`](../../canon/places/highwall-region-hydrology.md) | established | Water cycle; Dryrun; groundwater; floods; inland basin; hidden basin | Hydrology S01 C001-C019/C021-C023; A01 C001-C003; A02 C001; climate C003/C007/C014 | Traceable. All three lake referents, flood classes, and unknown mechanisms remain distinct. |
| [`highwall-region-ecology.md`](../../canon/places/highwall-region-ecology.md) | established | Regional structure; five environment/function sections; human influence | Ecology S01 C001-C017 | Traceable and species-neutral. It is the authoritative owner of the established wildfire relationship implicated by F04. |
| [`highwall-region-flora-and-fauna.md`](../../canon/places/highwall-region-flora-and-fauna.md) | working | Status; all inventories; human influence; disturbance; open records | Ecology S02 C001-C018; climate A01 C001 | Working authority is explicit and otherwise bounded. The disturbance repetition drifts from C014's `no-change` decision (F04). |
| [`upriver-highlands.md`](../../canon/places/upriver-highlands.md) | established | Summary; economy | Geography S01 C007-C008; geology C012; hydrology C018 link effect | Traceable. Hidden-basin discovery remains owned by hydrology; this page provides the recorded link rather than duplicating it. |
| [`stormlands.md`](../../canon/places/stormlands.md) | established | Summary; resources; hydrologic relationship | Geography S01 C009-C012/C023; climate C009 | Traceable. Working organism metadata does not promote the redwood analogue. |
| [`delta.md`](../../canon/places/delta.md) | established | Summary; water and agriculture | Geography S01 C020-C024 | Traceable. Both water relationships remain distinct. |
| [`forge.md`](../../canon/places/forge.md) | established | Summary; open issue | Geography S01 C013-C015 | Smelting/manufacturing is traceable. The word `downstream` lacks a reviewed authorizing claim (F02). |
| [`ledger.md`](../../canon/places/ledger.md) | established | Summary | Geography S01 C016-C019 | Traceable; detailed economic functions remain owned by the trade page. |
| [`regional-trade-system.md`](../../canon/economy/regional-trade-system.md) | established | Specialization; Highwall; currency; obligations | Geography S01 C001/C005-C006/C008/C010/C012-C021/C025-C027; A01 C003-C006 | Traceable. Local summaries and system ownership do not compete. |
| [`regional-imperial-structure.md`](../../canon/government/regional-imperial-structure.md) | established | Objective structure; official position | Geography A01 C001-C008 | Traceable. Objective, official, economic, and reader-reveal layers remain separated. |

Every canon page's front-matter provenance was compared with the reviews that
materially supply its current prose. Apart from the bounded findings below, no
missing review, canon-level mismatch, competing authoritative home, or
unbounded synthesis was found.

## Method

1. Parsed the generated index to establish counts, case membership, declared
   review authority, disposition, target, and navigation paths.
2. Read every source review and treated its claim table, amendments, files
   changed, deliberate non-changes, exception records, and outcome as the
   authoritative processing record.
3. For every claim, checked whether the declared repository effect exists at
   the recorded target, whether its scope matches, and whether later authority
   changes its current meaning.
4. Read every substantive canon page in full and mapped each factual passage
   to claim IDs, review authority, provenance metadata, and authoritative
   ownership. Synthesis was accepted only where each component remains bounded
   by reviewed claims.
5. Traced every correction, clarification, conflict resolution, and source
   completion through immutable source, review disposition, development
   record, current canon, and generated discovery.
6. Checked `no-change`, `out-of-scope`, `defer`, `conflict`, and proposal
   boundaries against story, design, open-question, proposal, contradiction,
   retired, and decision records.
7. Rechecked each candidate against later claims and exact immutable source
   text. Plausibility, chronology alone, reviewer rationale, and current prose
   were never substituted for authorial authority.

## Forward claim reconciliation

### Actionable dispositions

All 205 `create`, `update`, and `link-only` claims were examined at their
recorded targets. The overwhelming majority have complete, faithful effects:

- the Highwall, geology, climate, hydrology, ecology, working-organism,
  political, and economic authorities contain the claimed effects at the
  stated canon levels;
- page-level provenance includes the reviews that materially changed each
  page;
- specialized owners retain detailed explanations while overview and place
  pages use bounded contextual summaries and links; and
- later canyon, climate-boundary, and basin-identity clarifications are
  reflected in current canon without rewriting historical source records.

The exceptions are F01, where one component of Highwall S01-C005 is absent;
F02, where Forge contains a location claim not inventoried or authorized by
C013-C015; and F03, where generated navigation omits lifecycle relationships
even though the repository's authority-bearing records are correct.

### Non-action and exceptional dispositions

- All 36 `no-change` rows remain explainable through existing authority,
  administrative boundaries, source context, or later separately authorized
  claims. F04 is a bounded drift: the page nevertheless repeats the exact
  working-seed statement that the review said should remain only at the
  established owner.
- All three `out-of-scope` rows remain outside canon. Highwall S01-C023's
  general archive/discovery language has not become a story fact; the regional
  imperial reveal derives separately from geography A01 C010-C011.
- All 19 `defer` rows have the required open-question or proposal records.
  Current canon preserves their unknown or unapproved state.
- Hydrology S01-C016 has its required contradiction record. Hydrology A01-C002
  resolves the apparent conflict by distinguishing ancient and present lakes;
  current canon does not present the exceptional material incorrectly.
- No `retire` disposition exists in the accepted claim set. The retired area
  contains no substantive record, and no retired claim was found active in
  canon.

## Reverse canon reconciliation

Every substantive canon section is represented in the page table above. The
reverse pass found that:

- 12 of 13 pages contain no unidentified substantive assertion after claim,
  review, source, metadata, and ownership reconciliation;
- Forge contains the sole canon assertion for which no sufficient authorizing
  claim or source statement was found (F02);
- Highwall's passages are authorized, but one accepted component is absent
  rather than canon containing an unsupported component (F01);
- the working organism page clearly declares its level, but its wildfire
  sentence repeats an established fact contrary to the recorded no-change
  rationale (F04); and
- all other apparent repetitions are local consequences, bounded summaries,
  or navigation to a specialized owner rather than competing implementations.

The reverse pass did not demand claim IDs for headings, source lists, open
issue navigation, short statements identifying the linked detailed owner, or
connective wording that adds no independent setting assertion.

## Supersession-chain results

| Chain | Authority path | Current result |
| --- | --- | --- |
| Canyon origin | Highwall S01-C002 -> Highwall A01-C001 -> original-review amendment and resolved canyon-origin contradiction -> Highwall and geology canon | Canon correctly uses the megaflood model and preserves the historical claim. Generated navigation omits structured supersession state (F03). |
| Climate activity boundary | Climate S01 C018/C025 -> climate A01-C001 -> original-review amendment -> established climate wording and working flora/fauna scope | Established Blueleaf harvesting and reed cultivation are separated from working organism identity and biology. |
| Salt Basin identity | Climate S01-C012 plus geology C012-C016 -> climate A01-C002 -> original-review amendment -> geology identity owner and climate contextual use | Salt Basin is explicitly the inland basin where the clans live and is distinct from the hidden basin. |
| Inland-basin standing water | Geology C016 versus hydrology S01-C016 -> contradiction record -> hydrology A01 C001-C002 -> geology and hydrology canon | Ancient basin-filling lake and present smaller saline lake are correctly distinguished. Generated navigation does not surface the conflict record's resolved state (F03). |
| Old Wall flood cause | Highwall S01 C015-C016 -> hydrology A01-C003 -> hydrology A02-C001 -> hydrology question constraint and Highwall/hydrology canon | Canyon-entrance lake collapse and Old Wall flood are explicitly one event; no inferred causation remains. |
| Sovereignty source completion | Geography S01-C028 -> sovereignty open question -> geography A01-C001 -> regional government canon | Completed internal-affairs scope is correct and historical truncation remains auditable. Generated navigation leaves the earlier row labeled only `defer` (F03). |

## Findings

### `PROV-2026-08-07-F01` — Highwall corridor claim omits information flow

- **Category and severity:** Implementation narrower than authority —
  **Material**.
- **Canon page and section:** [`Highwall` — `Summary` and `Economy and
  infrastructure`](../../canon/places/highwall.md).
- **Review and claim:** [`Highwall Overview Seed Review`](../intake-reviews/2026-08-04-highwall-overview-s01-review.md),
  `CASE-2026-08-04-HIGHWALL-OVERVIEW-S01-C005`.
- **Disposition, target, and authority:** `update` targeting
  `canon/places/highwall.md`; review authority `establish-canon`, authority
  basis `explicit`.
- **Neutral discrepancy:** C005 establishes the canyon as the principal route
  and Highwall as the principal interface through which **people, goods, and
  information** pass. Current canon establishes the route, Highwall's trade
  interface, transportation, and coordination of people and resources, but
  contains no information-flow component. The exact immutable source confirms
  that information was a separate part of the authorized list.
- **Downstream impact:** Later communication, signaling, archive, trade, or
  political work could reasonably conclude that movement of information was
  never established, while the review says it was. This is incomplete
  implementation rather than authority for any specific communication system.
- **Verification performed:** Searched all canon for `information`, compared
  C005 with the complete source passage, reviewed the later corridor A02
  clarification, and checked Highwall's summary, economy, technology, related
  authorities, provenance, and change-log entries. No later claim narrows or
  supersedes this component.
- **Recommended successor action:** In a narrow author-authorized maintenance
  case, decide whether to add a bounded information-flow phrase to Highwall or
  explicitly correct the historical claim. Do not infer media, institutions,
  speeds, routes, or practices.
- **Prohibited inference:** This finding does not establish postal systems,
  signaling use outside the already listed technology, archives as regional
  communications infrastructure, or any operational detail.

### `PROV-2026-08-07-F02` — Forge is classified as downstream without reviewed authority

- **Category and severity:** Implementation broader than authority —
  **Material**.
- **Canon page and section:** [`Forge` — `Summary`](../../canon/places/forge.md).
- **Review and claims:** [`Regional Geography and Economy Seed Review`](../intake-reviews/2026-08-04-regional-geography-economy-s01-review.md),
  `CASE-2026-08-04-REGIONAL-GEOGRAPHY-ECONOMY-S01-C013` through `C015`.
- **Disposition, target, and authority:** `create`, targeting the Forge and
  regional-trade pages; review authority `establish-canon`, authority basis
  `explicit`.
- **Neutral discrepancy:** Forge's reviewed claims establish smelting,
  manufacturing, products, and imports from the Stormlands. Neither those
  claims nor the complete immutable source states that Forge is downstream.
  The canon sentence nevertheless begins, “Forge is a downstream place.” The
  page correctly says its more specific place type and location are not
  established, but that disclaimer does not authorize the broader downstream
  location.
- **Downstream impact:** Geography, routing, trade, government, or story work
  may treat Forge's side of Highwall as settled and derive spatial
  relationships that the accepted claim set does not provide.
- **Verification performed:** Compared all Forge occurrences in canon, the
  entire Forge source subsection, C013-C015, the review's changed-file record,
  trade dependencies, Stormlands export wording, and open geography records.
  Importing Stormlands materials and manufacturing downstream-region goods do
  not establish Forge's own location. No later claim supplies the missing
  relationship.
- **Recommended successor action:** Request explicit author authority either
  to establish Forge's broad location through new intake or to remove the
  unsupported qualifier through an authorized canon-correction case.
- **Prohibited inference:** Do not infer Forge's location from section order,
  imports, products, the location of other polities, or the word “downstream” used
  for other polities.

### `PROV-2026-08-07-F03` — Generated claim discovery omits lifecycle state

- **Category and severity:** Linkage gap — **Material**.
- **Canon pages and sections:** [`Highwall` — `Geography and environment`](../../canon/places/highwall.md),
  [`Regional Geology` — `Highwall canyon`](../../canon/places/highwall-region-geology.md),
  [`Regional Hydrology` — `Inland collapsed-lake basin`](../../canon/places/highwall-region-hydrology.md),
  and [`Regional Imperial Structure` — `Objective structure`](../../canon/government/regional-imperial-structure.md).
- **Reviews and claims:** Highwall S01-C002 and A01-C001; hydrology S01-C016
  and A01-C001/C002; geography S01-C028 and A01-C001.
- **Disposition, target, and authority:** The older rows remain `update`,
  `conflict`, and `defer`; the later claims are explicit `establish-canon`
  updates. Authority-bearing amendments, contradiction/question records, and
  canon targets are correct.
- **Neutral discrepancy:** The generated index exposes `review_authority` but
  not a row's `supersedes`, `superseded_by`, exceptional-record status, or
  later resolution. Highwall A01-C001's summary happens to say it replaces
  S01-C002, but the old C002 index row remains an unqualified accepted
  `update`. The hydrology conflict and sovereignty defer rows likewise do not
  expose that their linked records are resolved. A search beginning at an old
  row can therefore present stale lifecycle state until the reader manually
  follows several records.
- **Downstream impact:** Automated context building or a hurried incremental
  audit can recover an obsolete canyon origin, treat a resolved lake conflict
  as pending, or miss the completed sovereignty scope. Canon and source
  authority are correct; the risk is rediscovery of outdated authority paths.
- **Verification performed:** Inspected all relevant index rows and the
  generator schema, exact review `Supersedes` fields and amendments, both
  contradiction records, the resolved sovereignty question, current canon,
  and targeted discovery policy. No older claim currently changes canon, but
  the navigation artifact does not encode why.
- **Recommended successor action:** Add generated lifecycle fields and tests,
  preferably including forward `supersedes`, reverse `superseded_by`, and
  linked exceptional-record status. Keep the index explicitly
  non-authoritative and derive every value from reviews or development records.
- **Prohibited inference:** Do not change an old disposition, infer
  supersession from chronology, mark an exceptional record resolved without
  explicit authority, or treat generated state as canon.

### `PROV-2026-08-07-F04` — Working wildfire repetition drifts from `no-change`

- **Category and severity:** Target/disposition drift and duplicate
  implementation — **Minor**.
- **Canon pages and sections:** [`Regional Flora and Fauna` — `Disturbance`](../../canon/places/highwall-region-flora-and-fauna.md)
  and the authoritative [`Regional Ecology` — `Ecological functions and
  disturbance`](../../canon/places/highwall-region-ecology.md).
- **Review and claims:** Ecology S02-C014, with established authority supplied
  by ecology S01-C004.
- **Disposition, target, and authority:** S02-C014 is `no-change`, targets the
  established regional ecology page, and has `working-canon` review authority.
  Its rationale says the working seed does not need to duplicate or weaken the
  established fact.
- **Neutral discrepancy:** The working flora/fauna page nevertheless repeats
  that wildfire renews fire-adapted ecosystems. It labels the statement as
  consistent with the established regional disturbance pattern, so it does
  not presently compete with or weaken the owner, but the repository effect
  does not match the recorded non-action and the working page's provenance
  does not include the S01 review that established the fact.
- **Downstream impact:** Low-risk duplication can obscure which page and claim
  own the authority and can make an established fact appear to belong to a
  working inventory.
- **Verification performed:** Compared the exact S02 source statement, C014's
  disposition and rationale, both canon passages, both pages' canon levels,
  related links, provenance, and the S01-C004 authority. No later claim
  authorizes a second implementation.
- **Recommended successor action:** In safe editorial maintenance, remove the
  duplicate substantive sentence or replace the section with navigation to
  the established ecology owner, without changing the wildfire claim.
- **Prohibited inference:** Do not change wildfire frequency, geography,
  mechanism, affected organisms, or authority level.

## Verified traceable relationships

These negative results are retained because they cover high-risk authority
paths and make the audit reusable.

### `PROV-2026-08-07-V01` — Highwall canyon-origin supersession

- **Category:** Verified traceable.
- **Evidence:** Highwall S01-C002; geology C020/C021/C023; Highwall A01-C001;
  the S01 amendment; resolved canyon-origin contradiction; Highwall and geology
  prose; cumulative Highwall provenance and source links.
- **Result:** The megaflood model is current established canon, the modern
  river inherits the canyon, the older compound claim remains historical, and
  seasonal floods remain independently authorized by hydrology. F03 is a
  navigation limitation, not a defect in current canon authority.
- **Invalidated by:** Changes to any named claim or review amendment, the
  contradiction resolution, either canyon-formation passage, Highwall
  provenance, the canon level of either page, or generated supersession
  discovery.

### `PROV-2026-08-07-V02` — Climate agriculture and organism boundary

- **Category:** Verified traceable.
- **Evidence:** Climate S01 C018/C025; climate A01-C001; the S01 amendment;
  climate `Storm season and regional life`; flora/fauna `Status and scope`;
  ecology S02 authority and canon level.
- **Result:** Blueleaf harvesting and reed cultivation are established
  activities. Organism identities, biology, inventories, and detailed
  practices are not promoted and remain working or unestablished as stated.
- **Invalidated by:** Changes to C018/C025/A01-C001, either review's authority,
  the climate activity paragraph, working-page scope, flora/fauna canon level,
  organism aliases, or related proposal/question status.

### `PROV-2026-08-07-V03` — Salt Basin identity

- **Category:** Verified traceable.
- **Evidence:** Climate S01-C012; geology C012-C016; geography C007; climate
  A01-C002; geology `Inland basin`; climate `Climatic zones`; hydrology and
  ecology basin passages.
- **Result:** Salt Basin is the inland basin beyond Highwall where the clans
  live, and it is explicitly not the hidden basin. The identity is established
  in geology and used contextually elsewhere.
- **Invalidated by:** Changes to the named claims, climate amendment, basin
  terminology or aliases, geology ownership, clan-location claims, hidden
  basin identity, or provenance on climate/geology.

### `PROV-2026-08-07-V04` — Established and working ecology authority

- **Category:** Verified traceable, with bounded exception F04.
- **Evidence:** Ecology S01 C001-C017; ecology S02 C001-C018; both page levels
  and scope statements; organism proposal; both ecology questions; canon
  change log.
- **Result:** Zones, processes, functions, disturbance, and broad human
  influence are established. Named organisms and species-level roles are
  working. F04 is the only detected repetition that crosses the intended
  no-change boundary, and its qualifier still points to established authority.
- **Invalidated by:** Changes to either review authority, either page's canon
  level or scope, named organism claims, wildfire passages, organism
  terminology, or proposal/question status.

### `PROV-2026-08-07-V05` — Inland-basin lake and flood chronology

- **Category:** Verified traceable.
- **Evidence:** Geology C015-C021; hydrology S01 C006/C016/C021; hydrology A01
  C001-C003; hydrology A02-C001; resolved standing-water contradiction;
  geology, hydrology, and Highwall history.
- **Result:** The ancient basin-filling lake and megaflood, present smaller
  saline lake and decadal overflow, canyon-entrance lake and Old Wall flood,
  and ordinary or exceptional seasonal floods remain separate and correctly
  authorized.
- **Invalidated by:** Changes to any named event claim, the contradiction
  resolution, dates or frequency, identity or causal links among lakes and
  floods, affected canon sections, or relevant open-question constraints.

### `PROV-2026-08-07-V06` — Regional sovereignty and imperial relationship

- **Category:** Verified traceable.
- **Evidence:** Geography S01-C028; geography A01 C001-C008; resolved
  sovereignty question; government objective and official sections; trade
  imperial-obligation section; Highwall's attributed official account.
- **Result:** Each polity is internally sovereign while the region objectively
  functions as an imperial tributary province. Official diplomatic language
  is attributed and does not replace the objective structure.
- **Invalidated by:** Changes to the completion addendum, government or trade
  claims, sovereignty question state, internal-affairs qualification,
  imperial classification, official terminology, authoritative ownership, or
  any involved canon level.

### `PROV-2026-08-07-V07` — Highwall cross-domain overview

- **Category:** Verified traceable, with bounded exception F01.
- **Evidence:** Design A01 C002-C005; Highwall S01 C001-C022; corridor A02;
  geology C020-C023; hydrology S01 and A02; climate C008/C013; specialized
  body links and cumulative provenance.
- **Result:** Highwall's setting, people, institutions, economy, culture,
  technology, environment, Old Wall history, and attributed official history
  are bounded by reviewed authority. Specialized details remain at their
  owners. F01 is an omitted authorized component, not unsupported overview
  synthesis.
- **Invalidated by:** Changes to any supporting review, Highwall substantive
  section, residency or civic terminology, corridor scope, canyon or flood
  history, authority ownership, page level, provenance, or specialized-link
  relationships.

### `PROV-2026-08-07-V08` — Trade dependencies

- **Category:** Verified traceable, except Forge location in F02.
- **Evidence:** Geography S01 C001-C027; geography A01 C003-C006; all five
  place pages; trade page; government obligations; Highwall economy.
- **Result:** Specializations, imports, exports, currency exchange, Highwall
  intermediation, and imperial production obligations are authorized and
  owned by the trade page with bounded place summaries. Forge's manufacturing
  role is traceable even though its “downstream” location is not.
- **Invalidated by:** Changes to any specialization or dependency claim,
  place identities, exclusivity or scale language, currency practice,
  imperial obligations, trade ownership, aliases, or relevant page levels.

### `PROV-2026-08-07-V09` — Story-reveal boundaries

- **Category:** Verified traceable.
- **Evidence:** Geography A01 C007-C011; government `Official regional
  position`; complete regional-imperial reveal page; Highwall S01 C021-C023;
  empty character-knowledge and chronology indexes.
- **Result:** Objective politics, official belief, early reader framing, later
  reveal, and absent character knowledge remain separate. The story page does
  not invent an event, date, project, or character state.
- **Invalidated by:** Changes to C007-C011, government official language,
  story reveal wording or ownership, new character-knowledge or chronology
  records, Highwall's attributed history, or story/canon boundary policy.

## Deliberate non-findings

- The old river-formation claim is not a current canon contradiction; explicit
  A01 authority supersedes it. F03 concerns discovery metadata only.
- Blueleaf and reed activities on the established climate page do not promote
  biological identities or practices after climate A01.
- Salt Basin is not an unresolved alias and is not the hidden basin.
- The ancient basin lake, present saline lake, canyon-entrance lake, and their
  floods are not conflated.
- Internal sovereignty and tributary-province status are not contradictory;
  they apply at different scopes, while official language is attributed.
- Dryrun, its receiving perennial river, and the Stormlands-to-Delta river are
  not assumed to be the same.
- Highwall's highland resources do not contradict the Stormlands' status as
  largest regional timber and ore supplier; neither claim is exclusive.
- The hidden basin's agricultural capacity does not establish its retention
  mechanism, irrigation, or detailed climate.
- `related` metadata and short contextual summaries were not treated as
  competing authority where the detailed owner and canon level are clear.
- Missing distances, maps, quantities, names, taxonomies, mechanisms, and
  character knowledge are deliberate unknowns, not provenance failures.
- Older completed review publication fields were not treated as current-state
  defects; GitHub and Git history own publication state under current policy.

## Coverage limitations

- The regional map referenced by geography A01 is not present in the
  repository and was unavailable to the original review. This audit could
  verify only textual relative geography.
- The audit verifies repository authority, not scientific plausibility or
  completeness. No external research was used as evidence.
- Exact distances, quantities, taxonomy, hydrologic mechanisms, detailed
  climate, and undisclosed story knowledge cannot be traced because the corpus
  explicitly leaves them unestablished.
- Immutable submissions were read where review text was insufficient to decide
  scope; they were not treated as a replacement authority layer and were not
  modified.
- Claim-level coverage is semantic rather than a one-to-one sentence ledger.
  Compound canon sentences were accepted when every substantive component
  maps to reviewed claims; organizational prose was excluded as stated in the
  scope.
- GitHub draft-PR creation and checks occur after the report-only commit and
  push. Their state belongs in GitHub and the completion report, not a later
  audit-only commit.

## Reuse and invalidation conditions

A later audit may begin from audited commit
`027d0e36b8c20689b3d9fa0473f1860907720919`, inspect the complete Git diff to
its new baseline, and carry forward an individual result only after checking
all of its stated invalidation conditions.

At minimum, invalidate affected coverage when a later change touches or
semantically affects:

- a named claim, review amendment, authority declaration, disposition, target,
  or rationale;
- a substantive canon section, canon level, status, provenance list, alias,
  terminology, or ownership link involved in the relationship;
- a correcting or clarifying addendum, contradiction, decision, open question,
  proposal, retired record, story reveal, or design boundary;
- generated index schema, lifecycle fields, context output, or claim parsing;
  or
- a dependency that changes the meaning of an otherwise unchanged page, such
  as a place identity, event equivalence, political scope, river referent,
  working name, or established/working boundary.

An unchanged file is insufficient evidence for carrying a result forward.
The relationship and every authority-bearing dependency must remain unchanged
in meaning.

## Recommended successor tasks

1. **Forge location and Highwall information-flow authority case — author
   authority required; new intake only if establishing or correcting lore.**
   Resolve F02 first because unsupported spatial classification can propagate
   into geography, routing, economy, politics, and story. In the same narrow
   authority session, decide F01 without inventing communication details.
   Removing or adding canon still requires explicit authority even though the
   discrepancies are already evidenced.
2. **Claim-index lifecycle discovery — tooling improvement and safe process
   maintenance.** Add derived `supersedes`, `superseded_by`, and exceptional
   record status to generated navigation with validation tests, preserving
   reviews and development records as the authorities. This addresses F03 and
   reduces recurrence across future incremental audits without new lore.
3. **Working-page ownership cleanup — safe maintenance.** Resolve F04 by
   replacing the duplicate wildfire assertion with navigation to the
   established ecology owner. No new intake is needed if the task changes only
   links/duplication and makes no authority decision.

No action is recommended for V01-V09 or the deliberate non-findings unless an
invalidation condition occurs.

These rankings prioritize continuity and authority risk, downstream reach,
work possible without new lore, recurrence prevention, and expected value
relative to effort. No successor task was implemented in this branch.

## Retrospective

The corpus is substantially traceable: all 264 reviewed claims and all 13
substantive canon pages were reconciled, the three recently remediated Tier 3
authority issues are correct in current canon, and no critical finding remains.
The audit found three material and one minor issue. Two concern bounded text
coverage, one concerns generated lifecycle discovery, and one concerns a
low-risk duplicate. No contradiction, authority promotion, silent decision,
or broader systemic provenance failure was found.

The dominant remaining risk is not incompatible canon. It is the gap between
an authority-bearing historical record and the surfaces used to discover it:
one accepted component is absent, one canon qualifier lacks a claim, and
corrected lifecycle state is not machine-visible. The current owner/provenance
model otherwise supports reliable incremental review.

No canon, story, design, submission, intake review, claim index, canon change
log, proposal, open question, contradiction, decision, retired record,
template, script, or policy file was changed. No claim was added, removed,
promoted, reclassified, re-disposed, answered, or resolved.

## Validation and publication status

- [x] Repository validation passes against `origin/main` using the available
  Codex Python 3.12.13 runtime because `python` is not on `PATH`.
- [x] Generated claim index is current using the same runtime.
- [x] `git diff --check` passes.
- [x] Complete diff contains only this maintenance report.
- [x] Complete diff was inspected for invented lore, changed authority, silent
  contradiction resolution, submission mutation, unrecorded decisions, and
  unrelated changes.
- [x] Every canon content page and every intake review was considered.
- [x] All 264 indexed claims were reconciled.
- [x] Every candidate finding was checked against later authority and exact
  source text where required.
- [x] No setting, story, belief, historical, design, or policy claim was
  introduced.
- [x] No authority or contradiction decision was made.
- [ ] Draft pull request opened.
- [ ] `Canon and intake integrity` passes on GitHub.
- [ ] `Markdown style` passes on GitHub.

**Publication:** Pending. GitHub check history and final commit/PR state will
be reported externally and will not be copied into this audit through a
follow-up audit-only commit.
