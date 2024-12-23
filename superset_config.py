# Superset特有的配置
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

# Flask应用构建配置
# 你的应用密钥将用于安全登录回话cookie和在数据库里加密敏感信息
# 确保更改这个密钥为了你部署时使用一个安全的密钥
# 你可以使用`openssl rand -base64 42`创建一个更安全的密钥

SECRET_KEY = 'rRHjDsYjbrkZ5eBrXfchMbSenNhEydzzVUQmxvd4BM47YmUFGG'

# SQLAlchemy连接你的后台数据库
# 连接数据库的连接存储在superset的元数据里（slices,连接,表,仪表盘, ...）
# 注意：连接到数据源的连接，你可以通过Web页面直接进行管理

SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@postgres/superset'

# Flask-WTF的CSRF标识
WTF_CSRF_ENABLED = True
# 增加不需要CSRF保护的站点
WTF_CSRF_EXEMPT_LIST = []
# 一个一年有效期的CSRF令牌
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# 设置这个API密钥来使用Mapbox的可视化
MAPBOX_API_KEY = ''
