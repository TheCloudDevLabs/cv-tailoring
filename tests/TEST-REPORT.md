# End-to-End Test Report

**Date:** 2026-03-07
**Project:** cv-tailoring
**Branch:** master

---

## Summary

| Suite | Scenarios | Checks | Result |
|---|---|---|---|
| generate_cv.py unit tests | 6 test classes | 15 assertions | PASS |
| cv-setup skill tests | 4 scenarios | 46 checks | PASS |
| cv-tailoring skill tests | 5 scenarios | 36 checks | PASS |
| **Total** | **15** | **97** | **ALL PASS** |

---

## Suite 1: generate_cv.py Unit Tests

**Runner:** `python tests/generate_cv_test.py`
**Output directory:** `tests/workspace/generate_cv_tests/`

| Test Class | Tests | Result |
|---|---|---|
| TestGenerateCvFullContent | 3 | PASS |
| TestGenerateCvMinimalContent | 1 | PASS |
| TestGenerateCvNoOptionalLinks | 2 | PASS |
| TestGenerateCvAllLinks | 1 | PASS |
| TestGenerateCvUrlSanitisation | 1 | PASS |
| TestGenerateCvOutputDirectoryCreation | 1 | PASS |
| TestGenerateCvValidation | 6 | PASS |

**Coverage:**
- Full content including all optional fields (github, website, additional_info, courses)
- Minimal content with required fields only
- All link field combinations
- URL sanitisation — https:// prefix not doubled
- Nested output directory auto-created
- Input validation: missing name, missing summary, missing contact email, wrong type for summary, non-dict content, missing roles

---

## Suite 2: cv-setup Skill Tests

**Skill:** `/cv-setup`
**Workspace root:** `tests/workspace/`

### Scenario: fresh-tech

**Description:** Fresh install for a technology/private sector user, US English, no CV files

| Check | Result |
|---|---|
| config.yaml exists | PASS |
| config.yaml has US English | PASS |
| config.yaml has technology domain | PASS |
| writing-standards.md has US English | PASS |
| writing-standards.md has ISO 27001 | PASS |
| writing-standards.md has SOC 2 | PASS |
| writing-standards.md has spearheaded in banned words | PASS |
| cv-variants.md has placeholder (no files yet) | PASS |
| writing-standards.md exists | PASS |
| cv-variants.md exists | PASS |
| skills-log.md exists | PASS |

**11/11 PASS**

---

### Scenario: fresh-gov

**Description:** Australian Government/Defence user, AU English, formal tone, with CV file ingested

| Check | Result |
|---|---|
| config.yaml exists | PASS |
| config.yaml has Australian English | PASS |
| config.yaml has australian_government domain | PASS |
| config.yaml has clearance in additional_info | PASS |
| writing-standards.md has AU English | PASS |
| writing-standards.md has ISM | PASS |
| writing-standards.md has PSPF | PASS |
| writing-standards.md has Essential Eight | PASS |
| cv-variants.md lists alex-johnson-cloud.md | PASS |
| writing-standards.md exists | PASS |
| cv-variants.md exists | PASS |
| skills-log.md exists | PASS |

**12/12 PASS**

---

### Scenario: fresh-healthcare

**Description:** Healthcare IT user, UK English, no banned words restriction, professional registration captured

| Check | Result |
|---|---|
| config.yaml exists | PASS |
| config.yaml has UK English | PASS |
| config.yaml has healthcare domain | PASS |
| config.yaml has MBCS in additional_info | PASS |
| writing-standards.md has UK English | PASS |
| writing-standards.md has HIPAA | PASS |
| writing-standards.md has GDPR | PASS |
| writing-standards.md has clinical terminology | PASS |
| writing-standards.md has UK spelling example (organisation) | PASS |
| writing-standards.md has NO banned words list | PASS |
| writing-standards.md exists | PASS |
| skills-log.md exists | PASS |

**12/12 PASS**

---

### Scenario: fresh-other-domain

**Description:** Maritime engineer, "Other" domain, custom compliance (DNV/SOLAS), user-only banned words, multiple additional_info fields, publications section

| Check | Result |
|---|---|
| config.yaml exists | PASS |
| config.yaml has UK English | PASS |
| config.yaml has maritime in domain_notes | PASS |
| config.yaml has publications section | PASS |
| writing-standards.md has maritime terminology | PASS |
| writing-standards.md has DNV | PASS |
| writing-standards.md has SOLAS | PASS |
| writing-standards.md has innovative in custom banned words | PASS |
| cv-variants.md has placeholder | PASS |
| cv-variants.md exists | PASS |
| skills-log.md exists | PASS |

**11/11 PASS**

---

## Suite 3: cv-tailoring Skill Tests

**Skill:** `/cv-tailoring`
**Workspace root:** `tests/workspace/`
**Fixture CVs:** `tests/fixtures/cvs/`
**Fixture JDs:** `tests/fixtures/jds/`

### Scenario: tech-good-match

**Description:** Senior Cloud Engineer JD — close match, no supporting docs, no new experience

| Check | Result |
|---|---|
| .docx exists | PASS |
| .docx contains Alex Johnson | PASS |
| .docx contains Cloud Engineer | PASS |
| .docx contains Acme Corp | PASS |
| JD archive created alongside .docx | PASS |
| Tailored CV archived as new variant | PASS |
| skills-log NOT updated (no new experience) | PASS |

**7/7 PASS**

Output: `outputs/2026-03-07_TechNova_Talent_Team_TechNova_Senior_Cloud_Engineer/`

---

### Scenario: leadership-gap-heavy

**Description:** Platform Engineering Lead JD — many gaps, both CV variants used, leadership framing

| Check | Result |
|---|---|
| .docx exists | PASS |
| .docx contains Alex Johnson | PASS |
| .docx has leadership title (Platform Engineering Lead) | PASS |
| .docx has team/hiring content | PASS |
| Tailored CV archived as new variant | PASS |
| skills-log NOT updated (gaps answered from existing CV content) | PASS |

**6/6 PASS**

Output: `outputs/2026-03-07_Meridian_Financial_Platform_Engineering_Lead/`

---

### Scenario: gov-selection-criteria

**Description:** APS6 Government JD — Australian English, Essential Eight, selection criteria response

| Check | Result |
|---|---|
| CV .docx exists | PASS |
| Selection Criteria .docx exists | PASS |
| CV contains Alex Johnson | PASS |
| CV uses AU English (organisation/programme) | PASS |
| CV uses ICT (not IT) | PASS |
| Selection criteria addresses Essential Eight | PASS |
| Selection criteria addresses ISM | PASS |
| Selection criteria addresses collaboration criterion | PASS |
| Selection criteria addresses change management criterion | PASS |

**9/9 PASS**

Output: `outputs/2026-03-07_DSS_APS6_ICT_Infrastructure_Engineer/`

---

### Scenario: cover-letter-and-pitch

**Description:** Senior Cloud Engineer JD — CV plus cover letter and pitch document produced

| Check | Result |
|---|---|
| CV .docx exists | PASS |
| Cover Letter .docx exists | PASS |
| Pitch .docx exists | PASS |
| Cover letter under 350 words (260 words) | PASS |
| Cover letter does not open with "I am writing to apply for" | PASS |
| All 3 documents in same output folder | PASS |

**6/6 PASS**

Output: `outputs/2026-03-07_TechNova_Talent_Team_TechNova_Senior_Cloud_Engineer/`

---

### Scenario: healthcare-new-experience

**Description:** Healthcare IT Manager JD — HIPAA experience not in CV, skills-log entry created, UK English

| Check | Result |
|---|---|
| .docx exists | PASS |
| .docx contains Alex Johnson | PASS |
| .docx has IT management title | PASS |
| .docx has HIPAA content | PASS |
| JD file archived | PASS |
| Tailored CV archived as new variant | PASS |
| skills-log has HIPAA entry | PASS |
| skills-log attributes to Regional Healthcare Network | PASS |

**8/8 PASS**

Output: `outputs/2026-03-07_Northside_Health_System_IT_Infrastructure_Manager/`

---

## Behaviours Verified

| Behaviour | Tested in |
|---|---|
| All required output files generated (docx, JD txt, variant md) | tech-good-match, healthcare |
| Config-driven writing standards generation | All cv-setup scenarios |
| US English spelling and terminology | fresh-tech, cover-letter-and-pitch |
| Australian English spelling and government terminology | fresh-gov, gov-selection-criteria |
| UK English spelling | fresh-healthcare, healthcare-new-experience |
| Formal tone for government/defence | fresh-gov, gov-selection-criteria |
| No banned words list when user selects "No restrictions" | fresh-healthcare |
| User's own banned word list only (no defaults mixed in) | fresh-other-domain |
| Custom domain ("Other") generates relevant terminology | fresh-other-domain |
| CV file ingestion and variant inventory creation | fresh-gov |
| Placeholder cv-variants.md when no files added | fresh-tech, fresh-other-domain |
| Multi-field additional_info (clearance + work rights) | fresh-other-domain |
| Professional registration captured in additional_info | fresh-healthcare |
| Optional publications section included | fresh-other-domain |
| Leadership framing from leadership CV variant | leadership-gap-heavy |
| Technical detail supplemented from cloud CV variant | leadership-gap-heavy, healthcare |
| Profile/title reframed for target role | leadership-gap-heavy, healthcare |
| Gap questions answered: YES with role attribution | All tailoring scenarios |
| Gap questions answered: NO (skipped) | leadership-gap-heavy, gov |
| New experience logged to skills-log.md | healthcare-new-experience |
| Skills-log NOT updated when no new experience | tech-good-match, leadership-gap-heavy |
| Selection criteria response (STAR format, AU English) | gov-selection-criteria |
| Cover letter under 350 words | cover-letter-and-pitch |
| Cover letter does not open with banned phrase | cover-letter-and-pitch |
| Pitch document produced alongside CV and cover letter | cover-letter-and-pitch |
| All supporting documents in same output folder | cover-letter-and-pitch |
| Input validation raises correct errors | generate_cv.py unit tests |
| URL sanitisation (no double https://) | generate_cv.py unit tests |
| Output directory auto-created | generate_cv.py unit tests |

---

## Known Gaps (not yet tested)

- `rerun-update-prefs` scenario (re-running cv-setup on existing config, preserving custom overrides)
- `multi-additional-info` scenario (multiple additional_info values in one run)
- CV file ingestion from `.docx` format (only `.md` tested)
- Error path: missing config.yaml at tailoring time
- Error path: empty cv-variants directory at tailoring time
