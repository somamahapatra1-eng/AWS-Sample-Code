# AWS Integration & Multi-Tenant Architecture Portfolio

A technical portfolio site covering AWS concepts and CI/CD patterns with code samples.

## Structure

- `index.html` — Homepage with overview
- `concepts/` — Individual AWS concept pages (CloudFormation, IAM, SigV4 vs JWT, etc.)
- `cicd/` — CI/CD topics (Docker multi-arch, QEMU, packaging)

## Building

This is a static site. Serve it locally with:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment

Push to `somamahapatra1-eng.github.io` repo. GitHub Pages automatically serves `index.html`.

## References

- [harbor-events-sample](https://github.com/somamahapatra1-eng/harbor-events-sample) — Multi-tenant API on AWS
- [multiarch-image-ci](https://github.com/somamahapatra1-eng/multiarch-image-ci) — Docker pipeline for amd64 and arm64
