# Technical Baseline

Use this reference when implementation is in scope and the target frontend has no evidenced technology stack. The default output is a static high-fidelity V0 for customer review, written with enough engineering discipline that approved UI structure, components, mock-data semantics, and interaction expectations can be reused during production development.

## Selection Rules

1. Existing repository architecture, target platform, customer commitments, and review environment constraints win over this baseline.
2. Do not introduce a framework migration, a second UI system, or a competing library where the project already has a capable equivalent.
3. Apply the Web baseline only to a greenfield browser frontend. For a mini program, native app, embedded host, or constrained static review environment, use the native platform conventions and record the deviation.
4. Use mutually compatible current stable versions supported by the project's deployment environment. Do not pin a version from this document blindly.
5. Record the chosen baseline, deviations, and reason before the first implementation change.

## Default Web Baseline

| Concern | Recommended default | Boundary |
|---|---|---|
| Application framework | Next.js with React and TypeScript, using the App Router and static-export-compatible patterns when the review environment requires static output | Use the existing framework when present; use a platform-native runtime when the target is not a browser frontend |
| Product UI styling and primitives | Tailwind CSS with Radix-based or equivalent accessible primitives | Reuse the project's established design system or CSS approach |
| Operations or admin UI | Ant Design with Ant Design Pro Components | Use for greenfield React back-office workflows such as search, table, detail, edit, permission, and approval flows; do not combine it with a competing component system without a deliberate boundary |
| Icons | Lucide for product UI; `@ant-design/icons` for Ant Design admin UI | Reuse an existing approved icon set; do not mix families within one surface without a deliberate visual reason |
| Charts and maps | Apache ECharts | Use a domain-required chart/map SDK when binding requirements demand it; wrap charts behind a project component boundary |
| Tables | TanStack Table | Prefer the incumbent table component when it meets requirements |
| Forms and validation | React Hook Form with Zod | Use the platform's existing form and validation stack when present |
| Data boundary | Typed mock data modules or adapters shaped like future API responses | Keep mock data realistic and replaceable; do not hide product semantics inside component literals |
| Tests | Vitest with React Testing Library; Playwright for end-to-end and visual-runtime checks | Match the repository's existing runner and CI conventions |

## Implementation Rules

- Keep all product code in TypeScript; do not introduce untyped data boundaries without a documented reason.
- Centralize product tokens, data adapters, formatting, and chart options that are reused; keep page-specific composition local.
- Treat mock data as a first-class prototype asset: give it realistic ranges, empty/error/permission variants, source notes, and a shape that can later be swapped for API responses.
- Keep network calls optional in the V0. If the customer-review deliverable is static, avoid required live services and record where future API integration will attach.
- For operations or admin surfaces, prefer ProTable, ProForm, ProDescriptions, ProLayout, and ProCard when their established interaction and state models fit the approved content. Keep domain-specific workflow and metric semantics outside generic component configuration.
- Use one icon family per surface through a single project import convention, with accessible names or labels for interactive icons.
- Put ECharts in client-side components and dispose chart instances on unmount; define empty, loading, error, resize, and accessibility behavior for every material chart.
- Do not select a dependency merely because it is popular. The chosen tool must satisfy a confirmed product or platform need and fit the approved visual authority.

## Record

Add this decision to the active project artifact:

```markdown
## Technical Baseline

Review runtime: <static build, local preview, hosted preview, embedded host, or customer review constraint>
Selected stack: <framework, styling, UI primitives, icons, charts, data, tests>
Existing conventions retained: <list or none>
Deviations from the default: <decision and rationale, or none>
Future integration boundary: <mock data/adapters to replace, API assumptions, and productionization notes>
```
