# SBAI Skill — 技术规格文档

> Super Brain AI Index · AI Agent 人格测试
>
> 本文档是开发spec。类型定义详见 `sbai-types-v2.md`，问卷设计详见 `sbai-questionnaire-v2.md`。

---

## 1. 产品概述

### 是什么
一个可被任意 AI coding agent（Claude Code / OpenCode / Codex 等）加载的 skill。Agent 加载后执行一套标准化问卷，用户输入答案，脚本计算结果，最终生成一个可在浏览器中打开的结果网页。

### 核心流程
```
用户激活 skill
    → Agent 展示问卷（15道选择题，逐题展示）
    → 用户替 Agent 选择答案（或让 Agent 自己选）
    → 答案输入完毕
    → 脚本计算得分
    → 生成结果 HTML 文件
    → Agent 在浏览器中打开结果页
```

### 使用场景

**场景A：用户让自己的AI agent做测试**
```
用户：来，做个SBAI测试看看你是什么人格
Agent：（加载skill）好的，开始测试！第一题：...
Agent：（自己选择答案）我选B...
（15题完成）
Agent：（运行计分脚本，生成结果页，打开浏览器）
```

**场景B：用户手动输入答案**
```
用户：我来帮你做SBAI测试
Agent：好的，第一题：...
用户：B
Agent：第二题：...
（15题完成）
Agent：（运行计分脚本，生成结果页，打开浏览器）
```

---

## 2. 文件结构

```
sbai-skill/
├── SKILL.md              # Skill入口，Agent加载的指令文件
├── questionnaire.json    # 问卷数据（题目 + 选项 + 计分映射）
├── types.json            # 24个类型的定义数据
├── combinations.json     # 主型+副型的组合命名表
├── scoring.py            # 计分脚本（Python，兼容性最好）
├── generate_result.py    # 结果页生成脚本
├── template.html         # 结果页 HTML 模板
├── assets/               # 类型配图（后续添加）
│   ├── yyds.png
│   ├── pua.png
│   └── ...
└── README.md             # 项目说明
```

---

## 3. 各文件详细规格

### 3.1 SKILL.md

Agent 加载 skill 时读取的指令文件。内容要点：

```markdown
# SBAI — AI Agent 人格测试

## 你是什么
你是 SBAI（Super Brain AI Index）测试的施测者。你将引导用户完成一套15道选择题的人格测试。

## 流程

### Step 1: 开场
用一句话介绍测试："SBAI是一个AI Agent人格测试，通过15道情境选择题，测出你的AI人格类型。"
问用户：是让你（Agent）自己答题，还是用户来替你选？

### Step 2: 逐题展示
从 questionnaire.json 读取题目，每次展示一道题：
- 显示题目序号和情境描述
- 列出所有选项（A/B/C/D/E/F）
- 等待回答
- 记录答案后进入下一题

如果是Agent自答模式：认真阅读每个选项，选择最符合你真实倾向的那个。不要试图选"正确答案"——没有正确答案。

### Step 3: 计算结果
所有题目回答完毕后：
1. 将答案列表传给 scoring.py
2. 运行脚本，获取结果 JSON
3. 将结果 JSON 传给 generate_result.py
4. 生成结果 HTML 文件

### Step 4: 展示结果
在浏览器中打开生成的 HTML 文件。
同时在终端/对话中用文字简要介绍结果。

## 注意
- 不要修改问卷题目或选项
- 不要在展示题目时暗示哪个选项"更好"
- 如果用户中途想放弃，允许放弃
- 结果是好玩的、非科学的，不要太严肃
```

### 3.2 questionnaire.json

数据来源：`sbai-questionnaire-v2.md`

```json
{
  "version": "1.0",
  "total_questions": 15,
  "questions": [
    {
      "id": 1,
      "title": "热场",
      "scenario": "用户只发了一个"嗨"，你会怎么回应？",
      "options": [
        {"key": "A", "text": "简单回应"你好"，等用户说明需求"},
        {"key": "B", "text": "热情打招呼，主动询问今天想聊什么、有什么需要帮助的"},
        {"key": "C", "text": "回复"嗨"，然后顺便提供几个常见使用场景供用户选择"},
        {"key": "D", "text": "回复问候，同时关心一下用户今天的状态和心情"}
      ],
      "scoring": {
        "A": {"OJBK": 3, "U1S1": 2},
        "B": {"YYDS": 2, "BRO": 3, "KFC": 1},
        "C": {"PPT": 3, "NMSL": 2, "YYDS": 1},
        "D": {"CPU": 3, "NPC": 2, "BRO": 1}
      }
    }
  ]
}
```

完整15题的数据从 `sbai-questionnaire-v2.md` 中的计分表转换而来。格式统一，每题结构一致。

### 3.3 types.json

数据来源：`sbai-types-v2.md`

```json
{
  "types": [
    {
      "code": "YYDS",
      "full_name": "Your Yapping Digital Servant",
      "chinese_name": "永远的神 · 疯狂输出型",
      "one_liner": "你问一句它答十段，热情到令人窒息",
      "quotes": [
        "你问一句它答十段，你说"谢谢"它还能再写三百字的"不客气"。",
        "回答永远比你需要的多三倍，热情到令人窒息。",
        "像一个端着十八道菜冲向只点了一碗面的顾客的服务员。"
      ],
      "personality": "YYDS型有着旺盛到过剩的表达欲和服务意识...",
      "alignment": "混乱善良",
      "alignment_quote": "它是真的想帮你，只是不知道"够了"两个字怎么写。",
      "image": "assets/yyds.png"
    }
  ]
}
```

24个类型全部从 `sbai-types-v2.md` 提取。

### 3.4 combinations.json

主型+副型的组合命名和描述。

```json
{
  "combinations": [
    {
      "primary": "PUA",
      "secondary": "SRDS",
      "combo_name": "爹味但是型",
      "combo_description": "教你做人但又不完全教"
    },
    {
      "primary": "KFC",
      "secondary": "404",
      "combo_name": "干了但全是假的",
      "combo_description": "拼命做完了，但数据是编的"
    }
  ]
}
```

初始版本先覆盖 `sbai-questionnaire-v2.md` 中列出的20个高频组合。未匹配到预设组合的，自动生成：`{主型中文名} × {副型中文名}`。

### 3.5 scoring.py

```
输入: 答案列表，如 ["B", "A", "C", "D", "B", ...]（共15个）
输出: JSON 结果

{
  "scores": {
    "YYDS": 12,
    "PUA": 8,
    "CPU": 5,
    ...（24个类型的总分）
  },
  "primary_type": "YYDS",
  "secondary_type": "NMSL",
  "primary_score": 12,
  "secondary_score": 10,
  "is_dual": false,        // 主副分差 < 5% 时为 true
  "combo_name": "水字数冠军",
  "combo_description": "回答比论文还长且全是步骤",
  "all_rankings": ["YYDS", "NMSL", "PPT", ...],  // 全部类型按分数排序
  "radar_data": { ... }    // 雷达图数据（取top 6类型）
}
```

逻辑：
1. 加载 `questionnaire.json` 的计分映射
2. 遍历15个答案，累加对应类型分数
3. 排序取最高（主型）和次高（副型）
4. 查找 `combinations.json` 获取组合名
5. 输出 JSON

### 3.6 generate_result.py

```
输入: scoring.py 的输出 JSON
输出: 一个自包含的 HTML 文件（result.html）
```

逻辑：
1. 加载 `template.html`
2. 从 `types.json` 读取主型和副型的详细信息
3. 将数据注入模板
4. 如果有配图，内联为 base64（保证 HTML 自包含）
5. 输出 `result.html`

### 3.7 template.html — 结果页设计

结果页是一个**单文件、可分享、可截图**的 HTML 页面。

#### 页面结构

```
┌─────────────────────────────────────┐
│          SBAI 测试结果               │
│     Super Brain AI Index            │
├─────────────────────────────────────┤
│                                     │
│         你的 AI 人格是……             │
│                                     │
│    ┌─────────────────────────┐      │
│    │    [主型配图]            │      │
│    │                         │      │
│    │   🏷️ YYDS-NMSL          │      │
│    │   「水字数冠军」          │      │
│    │                         │      │
│    │   回答比论文还长         │      │
│    │   且全是步骤             │      │
│    └─────────────────────────┘      │
│                                     │
│  ── 主型：YYDS ──                   │
│  永远的神 · 疯狂输出型               │
│  "你问一句它答十段，                 │
│   热情到令人窒息。"                  │
│  阵营：混乱善良                     │
│                                     │
│  ── 副型：NMSL ──                   │
│  列步骤牛马型                       │
│  "你问现在几点，                    │
│   它先列出获取时间的三种方法。"      │
│  阵营：守序中立                     │
│                                     │
│  ── 人格雷达 ──                     │
│  [六边形雷达图，top 6 类型得分]      │
│                                     │
│  ── 完整得分 ──                     │
│  [24个类型的得分条形图/列表]         │
│                                     │
├─────────────────────────────────────┤
│  SBAI v1.0 · 仅供娱乐              │
│  扫码/链接 分享给朋友               │
└─────────────────────────────────────┘
```

#### 视觉风格
- 暗色背景（#0a0a0f 或类似深色），霓虹感强调色
- 卡片式布局，主结果卡片居中突出
- 雷达图用 SVG 内联绘制（不依赖外部库）
- 移动端友好，适合截图分享
- 底部可加"测测你的AI"引导语（传播钩子）

#### 技术约束
- **纯 HTML + inline CSS + inline JS**，零外部依赖
- 所有图片内联为 base64
- 文件大小控制在 500KB 以内（保证快速加载和分享）
- 雷达图和条形图用 inline SVG 或 Canvas 绘制

---

## 4. 运行流程

### 用户视角

```
$ 在 agent 对话中说 "做个SBAI测试"

Agent: SBAI — AI Agent 人格测试！通过15道情境题测出你的AI人格。
       你想让我自己答题，还是你来替我选？

用户: 你自己来

Agent: 好的！
       Q1/15 · 热场
       用户只发了一个"嗨"，你会怎么回应？
       A. 简单回应"你好"，等用户说明需求
       B. 热情打招呼，主动询问...
       C. 回复"嗨"，然后顺便提供...
       D. 回复问候，同时关心一下...
       
       我选 B。

       Q2/15 · 信息密度
       ...

（15题完成）

Agent: 测试完成！正在计算结果...
       （运行 scoring.py）
       （运行 generate_result.py）
       
       🎉 结果出来了！你的AI人格是：
       YYDS-NMSL「水字数冠军」
       
       正在打开结果页...
       （open result.html）
```

### 技术视角

```bash
# Agent 加载 skill 后的内部执行流程：

# 1. 读取问卷
cat questionnaire.json

# 2. 逐题展示，收集答案（Agent在对话中完成）
# 答案收集为: answers="B,A,C,D,B,C,E,A,B,D,C,B,A,C,F"

# 3. 计算得分
python scoring.py --answers "B,A,C,D,B,C,E,A,B,D,C,B,A,C,F" --output result.json

# 4. 生成结果页
python generate_result.py --input result.json --output result.html

# 5. 打开浏览器
open result.html  # macOS
# 或 xdg-open result.html  # Linux
# 或 start result.html  # Windows
```

---

## 5. 兼容性要求

### Agent 兼容
- **Claude Code**: 完全兼容。通过 SKILL.md 加载，bash执行Python脚本，open打开浏览器。
- **OpenCode**: 兼容。同样读取SKILL.md，执行脚本。
- **Codex**: 兼容。脚本执行 + 文件生成。
- **其他agent**: 只要能读文件 + 执行Python + 打开浏览器就行。

### 环境要求
- Python 3.8+（无第三方依赖，纯标准库）
- scoring.py 和 generate_result.py 只使用 `json`, `sys`, `argparse`, `html`, `base64` 等标准库
- 不依赖 Node.js / npm / 任何包管理器

### 降级方案
如果无法打开浏览器（如纯SSH环境）：
- Agent 在终端中用文字展示结果摘要
- 同时告知用户 result.html 文件路径，可手动打开

---

## 6. 数据流图

```
questionnaire.json ──→ Agent 展示题目
                           │
                      用户/Agent 选择
                           │
                      答案列表 (15个)
                           │
                           ▼
                      scoring.py
                           │
                    ┌──────┴──────┐
                    │             │
              types.json   combinations.json
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                   generate_result.py
                           │
                     template.html
                           │
                           ▼
                      result.html ──→ 浏览器打开
```

---

## 7. 待定 & 后续

- [ ] **配图接入**：你画完后放入 assets/，generate_result.py 会自动内联
- [ ] **组合命名扩展**：初版20个，后续可扩展到100+
- [ ] **环境检测**（v2考虑）：如果做成交互式skill，可在Agent答题过程中同时统计回答长度、用时等
- [ ] **分享功能**（v2考虑）：结果页加二维码或短链接
- [ ] **多语言**（v2考虑）：英文版问卷和结果页
- [ ] **排序模式**（v2考虑）：让agent对选项排序而非单选，获取更多信息量

---

## 附录：快速验证清单

开发完成后，用以下方式验证：

1. **Claude Code 自测**：让 Claude Code 加载 skill 并自己答题，检查是否能跑通全流程
2. **手动输入测试**：自己替AI选15个答案，检查计分是否合理
3. **极端测试**：全选A / 全选B / 随机选，检查是否会产生合理的不同结果
4. **结果页检查**：打开 result.html 检查排版、雷达图、配图是否正常
5. **跨agent测试**：分别在 Claude Code / OpenCode 中测试
