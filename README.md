# Проект "Обучающая платформа"

## Описание

Этот проект представляет собой обучающую платформу, где пользователи могут получать доступ к различным продуктам, а в этих продуктах - к урокам. Система также отслеживает статус просмотра уроков и время просмотра.

## Функциональные возможности

1. **Создание продуктов**:
   - Каждый продукт имеет владельца.
   - Можно управлять доступом пользователей к продукту.
   
2. **Управление уроками**:
   - Уроки могут быть добавлены к нескольким продуктам.
   - В уроках хранится базовая информация, такая как название, ссылка на видео и длительность просмотра.
   - Уроки могут быть просмотрены множеством пользователей, и для каждого просмотра фиксируется время и статус "Просмотрено"/"Не просмотрено". Если пользователь просмотрел 80% ролика, урок считается просмотренным.

3. **API-методы**:
   - Получение списка всех уроков по всем продуктам, к которым пользователь имеет доступ, с информацией о статусе и времени просмотра.
   - Получение списка уроков по конкретному продукту.
   - Отображение статистики по продуктам: количество просмотренных уроков, общее время просмотра, количество активных пользователей, процент приобретения продукта.

## Перспективы развития

1. **Расширенная система аналитики**: Подробная аналитика по активности пользователей, популярным урокам, прогрессу пользователей.
   
2. **Геймификация**: Внедрение системы достижений, наград и уровней для стимулирования пользователей продолжать обучение.
   
3. **Интеграция с другими платформами**: Подключение к внешним платформам для расширения контента, возможности импорта уроков.

4. **Персональные рекомендации**: Использование машинного обучения для предоставления персональных рекомендаций уроков на основе интересов и прогресса пользователя.
