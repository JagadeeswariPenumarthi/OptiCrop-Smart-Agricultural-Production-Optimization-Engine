# Scalability & Future Plan


## Current System Limitations

| S.No | Limitation | Impact | Priority to Address (High/Medium/Low) |
|---|---|---|---|
| 1 | Single crop prediction only, no alternatives shown | Reduces decision flexibility for farmers | Medium |
| 2 | Flask development server, not production-hardened | Not suitable for high-traffic public deployment | High |
| 3 | No persistent storage/history of past predictions | Cannot track usage trends over time | Low |
| 4 | Model trained on a single static dataset | May not generalize to all regional soil types | High |

## Scalability Plan

| S.No | Scalability Aspect | Current State | Proposed Upgrade / Solution |
|---|---|---|---|
| 1 | User Load | Single-instance local Flask server | Deploy behind Gunicorn + Nginx, or a managed cloud host (Render/Heroku/AWS) |
| 2 | Data Storage | Static CSV dataset | Move to a proper database (PostgreSQL) with support for regional dataset updates |
| 3 | Performance | Synchronous single-threaded inference | Add caching for repeated inputs; consider async request handling |
| 4 | Security | No authentication (by design) | Add rate-limiting if opened to public API access |

## Future Roadmap

| Phase | Planned Feature / Enhancement | Target Timeline | Expected Impact |
|---|---|---|---|
| Phase 2 | Top-3 crop recommendations with confidence scores | +1 sprint | Gives farmers more informed choices |
| Phase 3 | Fertilizer & irrigation optimization suggestions | +2 sprints | Extends value beyond crop selection alone |
| Phase 4 | Mobile-friendly / regional language support & cloud deployment | +3 sprints | Wider accessibility for real farmers |

