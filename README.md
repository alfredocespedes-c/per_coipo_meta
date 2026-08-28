# Forestin - Meta

Microservicio FastAPI para centralizar publicaciones de Forestin - Informa hacia Meta.

## Alcance POC

- Facebook
- Instagram
- Threads
- Modo `mock` por defecto, sin credenciales reales ni costos externos.
- Modo `live` preparado para conectar credenciales de Meta disponibles para pruebas.
- Autenticación interna mediante `X-API-Key`.
- GitHub se usa solo para código, versionamiento y CI; no GitHub Pages.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Abrir documentación Swagger en `http://127.0.0.1:8000/docs`.

## Endpoints iniciales

- `GET /health`
- `POST /facebook/posts`
- `POST /instagram/posts`
- `POST /threads/posts`
- `GET /status/{external_id}`

Los endpoints de publicación requieren header:

```text
X-API-Key: forestin-meta-poc
```

## Ejemplo

```json
{
  "app_name": "forestin_informa",
  "campaign_id": "INC-2026-001",
  "message": "CONAF informa actualización de incendio forestal.",
  "image_url": null
}
```

## Modos

`META_MODE=mock` devuelve publicaciones simuladas y permite desarrollar la integración completa sin tocar Meta.

`META_MODE=live` queda reservado para credenciales reales. La POC no incluye servicios pagados.

## Registro de avance

| # | Hito | Estado |
|---|---|---|
| M01 | Repositorio `per_coipo_meta` | ✅ |
| M02 | FastAPI + estructura modular | ✅ |
| M03 | `GET /health` | ✅ |
| M04 | Seguridad `X-API-Key` | ✅ |
| M05 | `.env.example` / configuración | ✅ |
| M06 | Cliente común Meta | ✅ base mock/live |
| M07 | Facebook | 🟡 endpoint listo / falta prueba real |
| M08 | Instagram | 🟡 endpoint listo / falta prueba real |
| M09 | Threads | 🟡 endpoint listo / falta prueba real |
| M10 | Historial / trazabilidad persistente | ⬜ |
| M11 | Docker | ✅ |
| M12 | Tests + GitHub Action | ✅ |
| M13 | Integración Forestin - Informa | ⬜ |

## Siguiente etapa

Configurar una app de Meta de prueba, cargar tokens mediante `.env`, validar permisos y realizar la primera publicación real empezando por Facebook.
