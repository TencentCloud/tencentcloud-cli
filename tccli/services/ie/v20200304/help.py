# -*- coding: utf-8 -*-
DESC = "ie-2020-03-04"
INFO = {
  "DescribeEditingTaskResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "编辑任务 ID。"
      }
    ],
    "desc": "获取智能编辑任务结果。"
  },
  "CreateEditingTask": {
    "params": [
      {
        "name": "EditingInfo",
        "desc": "智能编辑任务参数。"
      },
      {
        "name": "DownInfo",
        "desc": "视频源信息。"
      },
      {
        "name": "SaveInfo",
        "desc": "结果存储信息。对于包含智能拆条、智能集锦或者智能封面的任务必选。"
      },
      {
        "name": "CallbackInfo",
        "desc": "任务结果回调地址信息。"
      }
    ],
    "desc": "创建智能编辑任务，可以同时选择视频标签识别、分类识别、智能拆条、智能集锦、智能封面和片头片尾识别中的一项或者多项能力。"
  }
}