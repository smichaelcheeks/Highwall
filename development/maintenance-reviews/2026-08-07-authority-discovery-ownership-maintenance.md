# Maintenance Review: Authority Discovery and Ownership Links

## Scope

- **Objective:** Remediate Tier 3 findings `T3-2026-08-07-F04` through
  `T3-2026-08-07-F07` by surfacing review authority in generated claim
  discovery, curating Highwall's central authority links, completing two
  human-readable provenance lists, and refreshing one resolved record.
- **Why this is maintenance:** The work changes navigation and process
  metadata only. It introduces no lore, changes no claim's authority or
  disposition, resolves no contradiction, and makes no sovereignty decision.
- **Impact:** Claim-index schema version 2 and targeted context expose the
  authority already declared by each intake review. Canon and development
  pages receive only links or lifecycle metadata.

## Files inspected

The Tier 3 audit findings and successor ranking; claim-index and targeted
context generators; consistency workflow; all intake-review authority values;
Highwall and the seven specialized authorities that link to it; Hydrology and
Stormlands provenance and source sections; and the resolved sovereignty record
and regional government authority.

## Changes

- Add `review_authority` to every generated claim row, increment the generated
  schema to version 2, and display the field in targeted context.
- Document that the field aids discovery while the linked review remains the
  authority.
- Add a restrained reciprocal set of seven regional authorities to Highwall's
  `related` metadata and a navigation-only body section.
- Add the already-valid climate review to the Hydrology and Stormlands
  human-readable source lists.
- Replace the sovereignty record's future placeholder with the existing
  government authority and link it from front matter.

## Deliberate non-changes

- No claim classification, disposition, authority basis, review authority, or
  canon level changes.
- No substantive explanation is copied into Highwall, and `related` is not
  treated as an exhaustive taxonomy or made universally reciprocal.
- No hydrology, climate, ecology, organism, trade, government, sovereignty, or
  story statement changes.
- The Tier 3 audit remains an unchanged historical snapshot.

## Verification

- [x] No setting, story, belief, historical, or design claim was introduced.
- [x] No authority or contradiction decision was made.
- [x] Relevant deterministic validation passed.
- [x] The complete diff contains no unrelated changes.
- [x] Publication status is reported from GitHub rather than copied into an
  audit-only commit.

Additional verification checks that all generated working-ecology rows expose
`review_authority: working-canon` and that targeted context prints that value.

## Publication

Pending.
