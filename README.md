# RS AI - Content Factory

Pipeline automatisé pour produire, packager, exporter et mesurer des contenus vidéo (TikTok / YouTube / LinkedIn).

## Quickstart (local)
1. Prérequis: Docker, Python 3.12+, ffmpeg installé
2. Lancer n8n:
   - docker compose up
3. Lancer le worker:
   - cd apps/worker
   - python -m venv .venv && source .venv/bin/activate
   - pip install -U pip
   - pip install -e .
   - python -m rsai_worker.main

## Philosophie
- Orchestration: n8n
- Exécution: worker Python (pipeline modulaire)
- Conformité: validation humaine avant publication quand l'API officielle n'est pas fiable/disponible
