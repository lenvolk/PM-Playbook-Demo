# ADO snippet: Acceptance criteria (Given/When/Then)

Use this pattern for testable acceptance criteria.

---

- Given <precondition>
  - And <additional precondition>
- When <user/system action>
- Then <expected result>
  - And <additional expected result>

Notes:
- Prefer multiple small criteria over one large paragraph.
- Include error/empty/loading states where relevant.
