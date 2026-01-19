from pathlib import Path
import json
from datetime import datetime

def run_pipeline(job: dict) -> dict:
    # MVP: on ne génère rien encore, on produit un "artifact package"
    out_dir = Path("outputs") / job["job_id"]
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "job": job,
        "created_at": datetime.utcnow().isoformat(),
        "artifacts": {
            "video": str(out_dir / "video.mp4"),
            "captions": str(out_dir / "captions.srt"),
            "packaging": str(out_dir / "packaging.json"),
        },
        "status": "EXPORT_ONLY_MVP"
    }

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return {"job_id": job["job_id"], "status": "ok", "out_dir": str(out_dir)}
