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
usuarios_atividade
```

### 🧠 Fazer o join igual ao seu caso

```promql
usuarios_info * on(id) group_left(pais, plano) (usuarios_atividade or on() vector(0))
```

👉 Isso vai:

- Juntar as duas métricas pelo label `id`.
- Trazer `pais` e `plano` da `usuarios_info`.
- Substituir valores ausentes de `usuarios_atividade` por 0.

Resultado esperado (algo assim):

```
{ id="1", pais="BR", plano="premium" } 8
{ id="2", pais="US", plano="free" } 0
{ id="3", pais="BR", plano="free" } 5
```

---

## Grafana

- http://localhost:3000

---

## 1️⃣ Adicionar o Prometheus como datasource no Grafana

1. Abra o Grafana: [http://localhost:3000](http://localhost:3000) (se estiver usando a versão padrão do Grafana via Docker, porta 3000).
2. Faça login (usuário/padrão: `admin` / `admin`).
3. Vá em **Configuration → Data Sources → Add data source → Prometheus**.
4. Configure:

   - URL: `http://prometheus:9090` (ou `http://localhost:9090` se estiver rodando fora do Docker network).
   - Clique em **Save & Test**. Deve mostrar `Data source is working`.

---

## 2️⃣ Criar um dashboard com suas métricas

1. Vá em **Create → Dashboard → Add new panel**.
2. No campo de query do painel, use sua query do Prometheus. Por exemplo:

```promql
usuarios_info * on(id) group_left(pais, plano) (usuarios_atividade or on() vector(0))
```

- Isso vai gerar a métrica com labels `id`, `pais`, `plano` e o valor da atividade.

3. Configure a visualização:

   - Tipo: **Table** ou **Bar Gauge** (depende de como quer mostrar os usuários).
   - Se usar **Time series**, pode precisar somar ou agrupar:

     ```promql
     sum by(pais, plano) (usuarios_info * on(id) group_left(pais, plano) (usuarios_atividade or on() vector(0)))
     ```

     - Isso mostra total de atividade por país e plano.

---

## 3️⃣ Ajustar labels e exibição

- No **Table Panel**, você pode mostrar:

  - `id`, `pais`, `plano` e `value` como colunas.

- No **Graph Panel** ou **Bar Chart**, você pode usar `pais` ou `plano` como eixo X e `value` como Y.
- Use **Legend → {{pais}} - {{plano}}** para diferenciar os usuários.

---

## 4️⃣ Atualização automática

- Configure **Refresh Interval** do painel, por exemplo **5s**, para acompanhar a atualização em tempo real do seu exporter.

---
