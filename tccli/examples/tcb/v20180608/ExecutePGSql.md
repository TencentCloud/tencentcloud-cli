**Example 1: 创建表**



Input: 

```
tccli tcb ExecutePGSql --cli-unfold-argument  \
    --EnvId pg-mikejliu-0g9cqmar358527a9 \
    --Sql CREATE TABLE test_products (
    id SERIAL PRIMARY KEY,                        -- 产品唯一标识
    sku VARCHAR(20) UNIQUE NOT NULL,             -- 库存单位编码，唯一且必填
    name TEXT NOT NULL,                          -- 产品名称
    category VARCHAR(50),                        -- 分类
    price NUMERIC(12, 2) NOT NULL DEFAULT 0.00,  -- 单价
    stock_quantity INTEGER DEFAULT 0,            -- 库存数量
    tags JSONB,                                  -- 标签（使用 JSONB 存储扩展属性）
    last_updated TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() -- 最后更新时间
);
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
        "Columns": null,
        "ExecutionTimeMs": 34,
        "Rows": null,
        "RequestId": "5cf1d355-cdb7-4879-bd22-4e89ddc10095"
    }
}
```

**Example 2: 查询表字段**



Input: 

```
tccli tcb ExecutePGSql --cli-unfold-argument  \
    --EnvId pg-mikejliu-0g9cqmar358527a9 \
    --Sql select column_name FROM information_schema.columns WHERE table_schema = 'public'   AND table_name = 'test_products'
```

Output: 
```
{
    "Response": {
        "AffectedRows": 0,
        "Columns": [
            "column_name"
        ],
        "ExecutionTimeMs": 58,
        "Rows": [
            "[\"id\"]"
        ],
        "RequestId": "21b3df84-7ea3-4487-9583-e4de88b4ab89"
    }
}
```

