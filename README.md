# Prometheus-SIM

---

## 🚀 Rodar

```bash
docker compose down -v
docker compose up --build
```

Acesse:

- Exporter: [http://localhost:8000/metrics](http://localhost:8000/metrics)
- Prometheus UI: [http://localhost:9090](http://localhost:9090)

---

## 🔍 Testando queries no Prometheus

### 🧱 Ver todas as métricas

```promql
usuarios_info
usuarios_endereco
```

### 🧠 Fazer o join

```promql
usuarios_info * on(id) group_left(rua, numero, cidade, estado, pais) usuarios_endereco
usuarios_info{id="1"} * on(id) group_left(rua, numero, cidade, estado, pais) usuarios_endereco{id="1"}
```

---

## Grafana

- http://localhost:3000

---

## Adicionar o Prometheus como datasource no Grafana

1. Abra o Grafana: [http://localhost:3000](http://localhost:3000) (se estiver usando a versão padrão do Grafana via Docker, porta 3000).
2. Faça login (usuário/padrão: `admin` / `admin`).
3. Vá em **Configuration → Data Sources → Add data source → Prometheus**.
4. Configure:

   - URL: `http://prometheus:9090` (ou `http://localhost:9090` se estiver rodando fora do Docker network).
   - Clique em **Save & Test**. Deve mostrar `Data source is working`.

---

## Font family

- https://fonts.google.com/selection?preview.text=Testando

---

## Plugins

- HTML graphics
- Business Text
