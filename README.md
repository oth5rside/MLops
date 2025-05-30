# Final task

Цель проекта: разработать конвеер машинного обучения data-продукта (Web или API приложение)

Требования к реализации проекта:

Исходные коды проекта должны находиться в репозитории GitHub.
Проект оркестируется с помощью ci/cd (jenkins или gitlab).
Датасеты версионируются с помощью dvc и синхронизируются с удалённым хранилищем.
Разработка возможностей приложения должна проводиться в отдельных ветках, наборы фичей и версии данных тоже.
В коневеере запускаются не только модульные тесты, но и проверка тестами на качество данных.
Итоговое приложение реализуется в виде образа docker. Сборка образа происходит в конвеере.
В проекте может использоваться предварительно обученная модель. Обучать собственную модель не требуется.

## 🛠️ Требования
- Python 3.9+
- DVC 3.0+
- Docker (опционально)
- Аккаунт Google (для DVC с Google Drive)

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/oth5rside/MLops
cd MLops