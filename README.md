# shiep-yjsgl
本系统封装了来自【上海电力大学研究生信息系统】的部分常用功能（见API列表），采用Flask框架构建后台应用 <br>

* 【目前提供的功能】：

|   功能名称              |              url              |
| ---------------------  | ----------------------------- |
|  成绩查询               |         /grade_query          |
|  获取所有需评教课程信息  |         /pj_lesson_query      |
|  获取课程评教表          |        /pj_table_query       |
|  提交评教               |        /post_pj              |

* 【启动方式】: 进入根目录，在控制台输入命令 ```python app.py```


### 说明
为了更便于与上海电力大学研究生信息系统对照使用与阅读，本代码中大部分的【变量命名】采取【直接照搬上海电力大学研究生信息系统】的办法（所以如果命名太丑不是本作者的锅啦啦啦：）

-----------------------------------------------------------------------------

### API列表
#### 成绩查询
* url: /grade_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx}
  * username: 学号;
  * password: 密码;

#### 获取所有需评教课程信息
* url: /pj_lesson_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx}
  * username: 学号;
  * password: 密码;

#### 获取课程评教表
* url: /pj_table_query
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "bjid": xxxxx, "jsbh": xxxx}
  * username: 学号;
  * password: 密码;
  * bjid: 班级id;
  * jsbh: 教师编号;

#### 提交评教
* url: /post_pj
* 请求类型: POST
* 接收参数: {"username": xxxxxxxxx, "password": xxxxxxxxxxx, "bjid": xxxxx, "jsbh": xxxx, "pj_json": xxxxxxx} <br>
  * username: 学号;
  * password: 密码;
  * bjid: 班级id;
  * jsbh: 教师编号;
  * pj_json: 学生提交的评教内容（json字符串）<br>
    【示例】 其中 bjid为班级id；jsbh为教师编号；zbid为指标id；zt为状态；df为得分 <br>
    pj_json = [ <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "1", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "2", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "3", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "4", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "5", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "6", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "7", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "8", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "9", "zt": "1", "df": "8.0"}, <br>
      {"bjid": "2f33246b-00bb-4067-9d0b-f682b9c06fab", "jsbh": "2020010004", "zbid": "10", "zt": "1", "df": "8.0"} <br>
    ] 
