# ProofStack Phase 3A — Authentication Architecture

**Status:** Accepted for Phase 3A implementation  
**Scope:** Core email/password authentication only. Google and GitHub OAuth remain Phase 3B.

## Decision

Use opaque, server-managed sessions with a random browser cookie and PostgreSQL-backed session records. Do not use JWT access/refresh tokens for this browser-first flow.

## Request lifecycle

1. On successful login, generate a cryptographically random session secret.
2. Send the secret only in an HttpOnly cookie.
3. Persist only a SHA-256 digest of the secret in the session table; never persist the raw cookie secret.
4. For protected requests, hash the presented cookie secret and look up a non-expired, non-revoked session. Resolve its user through the foreign key.
5. On logout, revoke the current session and clear the cookie.
6. On password reset/change, revoke existing sessions so old credentials cannot keep access.

The session record will include a user foreign key, token digest, expiry, creation timestamp, optional revocation timestamp and optional last-used timestamp. The table will be introduced with the session lifecycle implementation step.

## Cookie and request protections

- Cookie is HttpOnly and uses Path=/.
- Use Secure in production; local HTTP development must remain usable.
- Use SameSite=Lax for the intended same-site browser deployment.
- Configure CORS to allow only the configured frontend origin and credentials; never use wildcard origins with credentialed requests.
- Validate Origin and use CSRF protection for state-changing cookie-authenticated requests.
- Do not put session secrets in URLs, JSON responses, logs or browser-accessible storage.
- Keep session expiry and invalidation enforced by the backend, not by the cookie alone.

If production frontend and backend are deployed on different sites, cookie SameSite and CSRF settings must be reviewed for that topology before deployment.

## User/account model

The initial users table contains only authentication identity and account lifecycle fields:

- id: UUID primary key.
- email: normalized email address, unique and required.
- password_hash: nullable hash field. Email/password accounts populate it; nullable storage keeps the core account model compatible with future OAuth-only accounts.
- email_verified_at: nullable timestamp indicating verified email.
- is_active: account enabled/disabled flag.
- created_at and updated_at: timezone-aware timestamps.

Email normalization and validation occur in the application layer; uniqueness is enforced by PostgreSQL. Passwords are never stored in plaintext. Authentication tokens and session secrets are stored as digests only.

## Future OAuth compatibility

Phase 3B can associate external Google/GitHub identities with the same internal user using a separate identity-linking model. OAuth is not implemented in Phase 3A. Do not add provider-specific columns to the user table now.

## Email delivery

Keep delivery behind a small email-sender interface. Automated tests use a fake sender. Development may use a development-only console adapter for verification/reset links; it must be impossible to select that adapter in production. Production requires explicitly configured email delivery. Never log passwords or raw session secrets.

## Boundaries

This decision does not authorize student profiles, assessments, projects, repository access, AI features, recruiter features, microservices or Phase 3B OAuth. Phase 1 and Phase 2 remain locked. All schema changes use Alembic migrations.
