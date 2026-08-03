**Example 1: GetExampleDetail**

获取

Input: 

```
tccli dlc GetExampleDetail --cli-unfold-argument  \
    --ExampleId example-001-ray-core-basics
```

Output: 
```
{
    "Response": {
        "Category": "quickstart",
        "CodeArchiveUrl": "https://common-job-packages-251233710.cos.ap-guangzhou.myqcloud.com/models/examples/example-001-ray-core-basics.zip",
        "CreateTime": 1779799361632,
        "Deleted": 0,
        "Description": "通过简单案例快速掌握Ray的三大核心概念：Task、Actor和Object",
        "Difficulty": "beginner",
        "EstimatedTime": 15,
        "ExampleId": "example-001-ray-core-basics",
        "Id": 11,
        "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
        "IsEnabled": true,
        "LabImage": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu-lab",
        "Popularity": 12,
        "Readme": "# Ray Hello World：5 分钟掌握分布式计算三大核心原语\n\n本案例是 Ray 案例广场的 **Hello World**。只需 5 分钟，通过交互式 Notebook 快速掌握 Ray 的三大核心原语——**Task**（异步任务）、**Actor**（有状态服务）与 **Object**（分布式对象）。\n\n## 一、案例概览\n\n| 维度 | 说明 |\n| --- | --- |\n| 目标人群 | 刚接触分布式计算的开发者、数据科学家、系统架构师 |\n| 核心价值 | Ray 像是 Python 的“超级并发库”——无需学习 MPI 等底层通信框架，只需在函数或类上添加 `@ray.remote`，即可将单机代码无缝扩展到集群 |\n| 学习成本 | 代码改动量通常 < 5%，即可获得接近线性的水平扩展能力 |\n\n## 二、三大核心原语\n\n在 Ray 的世界里，只需掌握以下三个原语，就能构建从简单脚本到复杂分布式系统的各类应用：\n\n```mermaid\ngraph LR\n    A[\"@ray.remote<br/>装饰器\"] --> B[\"Task<br/>异步任务\"]\n    A --> C[\"Actor<br/>有状态服务\"]\n    A --> D[\"Object<br/>分布式对象\"]\n```\n\n### 1. Task —— 异步任务\n\n将普通 Python 函数变为可在集群任意节点上运行的 **异步任务**。\n\n| 特性 | 说明 |\n| --- | --- |\n| 无状态 | 每次调用相互独立，天然适合并行 |\n| 异步调用 | 调用后立即返回 `ObjectRef`，不阻塞主线程 |\n| 典型场景 | 并行数据处理、大规模数值计算、蒙特卡洛模拟 |\n\n### 2. Actor —— 有状态服务\n\n将 Python 类变为运行在集群中的 **有状态服务进程**。\n\n| 特性 | 说明 |\n| --- | --- |\n| 有状态 | 在多次调用之间保持内部状态（如模型权重、计数器） |\n| 串行执行 | 同一 Actor 的方法调用按序执行，保证状态一致性 |\n| 典型场景 | 模型推理服务、参数服务器、数据库连接池、强化学习环境 |\n\n### 3. Object —— 分布式对象\n\nRay 基于底层 **Plasma Object Store** 提供高效的跨进程数据共享：\n\n| API | 功能 |\n| --- | --- |\n| `ray.put(obj)` | 将数据放入共享内存，返回 `ObjectRef`（引用 ID） |\n| `ray.get(ref)` | 根据引用 ID 取回数据 |\n\n> **性能亮点**：同一节点上的 Worker 可通过 **零拷贝（Zero-Copy）** 直接访问数据，大对象（矩阵、图片等）的传递效率极高。\n\n## 三、快速上手\n\n点击右上角 **“立即启动”** 按钮，即可进入预置好的 Jupyter Notebook 环境。以下是核心代码片段：\n\n### Step 1：初始化 Ray\n\n```python\nimport ray\n\nif not ray.is_initialized():\n    ray.init()\nprint(f\"集群资源: {ray.cluster_resources()}\")\n```\n\n### Step 2：体验 Task（异步任务）\n\n将一个简单的平方计算函数变为分布式任务，4 个任务并行执行，耗时约 1 秒（串行需 4 秒）：\n\n```python\n@ray.remote\ndef square(x):\n    time.sleep(1)\n    return x * x\n\nfutures = [square.remote(i) for i in range(4)]   # 并行提交\nresults = ray.get(futures)                        # 阻塞获取结果\n```\n\n### Step 3：体验 Actor（有状态服务）\n\n创建一个分布式计数器，即使并发调用也能保证状态一致：\n\n```python\n@ray.remote\nclass Counter:\n    def __init__(self):\n        self.count = 0\n\n    def increment(self):\n        self.count += 1\n        return self.count\n\ncounter = Counter.remote()\nfutures = [counter.increment.remote() for _ in range(10)]\nprint(ray.get(futures))   # [1, 2, 3, ..., 10]\n```\n\n### Step 4：体验 Object（共享内存）\n\n将大数组放入共享内存，多个 Task 可零拷贝访问同一份数据：\n\n```python\nimport numpy as np\n\nlarge_array = np.random.rand(1000, 1000)\nobj_ref = ray.put(large_array)   # 放入对象存储\n\n@ray.remote\ndef sum_array(arr):\n    return arr.sum()\n\nresult = ray.get(sum_array.remote(obj_ref))   # 零拷贝读取\n```\n\n## 四、核心概念速查表\n\n| 概念 | 本质 | 关键 API | 状态 |\n| --- | --- | --- | --- |\n| **Task** | 远程函数 | `@ray.remote` → `.remote()` → `ray.get()` | 无状态 |\n| **Actor** | 远程类 | `@ray.remote` (类) → `.remote()` → `ray.get()` | 有状态 |\n| **Object** | 共享内存 | `ray.put()` → `ray.get()` | — |\n\n## 五、延伸阅读\n\n- [Ray Core 官方文档](https://docs.ray.io/en/latest/ray-core/walkthrough.html) — 完整 API 参考与进阶指南\n- [Ray 设计模式](https://docs.ray.io/en/latest/ray-core/patterns/index.html) — 常见分布式编程模式与最佳实践\n",
        "ResourceConfig": "{\"Head\":{\"Name\":\"default-head\",\"PodCpu\":4,\"PodMem\":2,\"PodNum\":1},\"Worker\":[{\"Name\":\"default-worker\",\"PodCpu\":1,\"PodMem\":2,\"MinPodNum\":4,\"MaxPodNum\":4}]}",
        "SortOrder": 1,
        "Tags": [
            "Ray Core"
        ],
        "Title": "Ray入门，你的第一个分布式作业",
        "UpdateTime": 1779799361632,
        "RequestId": "080d3154-74fe-491d-862c-41bb43161735"
    }
}
```

