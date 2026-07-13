# Arsitektur Komponen, Skema Database, dan Mitigasi Lanjutan (Tahap 1 & 3)

Dokumen ini memuat landasan teori teknis, skema penyimpanan data, diagram arsitektur, serta mekanisme resiliensi untuk sistem resolusi kunci JWKS yang dilengkapi mitigasi flooding.

---

## 1. Diagram Arsitektur Komponen

Arsitektur ini memisahkan layer API Gateway (penyaring utama), Redis (caching performa tinggi), dan PostgreSQL (storage persisten).

```mermaid
graph TD
    Client[Klien / Aplikasi] -->|Request + JWT| Gateway[API Gateway / Auth Service]
    
    subgraph Caching Layer (In-Memory)
        Gateway -->|1. Cek Cache / Rate Limit| Redis[(Redis Cache)]
    end
    
    subgraph Storage Layer (Persisten)
        Gateway -->|2. Cache Miss / Fetch fallback| DB[(PostgreSQL)]
        Gateway -->|3. JWKS Fetch Failure| IdentityProvider[External Identity Provider / IdP]
    end
    
    Redis -.->|Sinkronisasi Keys & Counters| Gateway
    DB -.->|Sinkronisasi State| Gateway