# AI for Skeptics — A Self-Paced AI Course for Business School Faculty

## Visuals

<img width="1081" height="748" alt="Screenshot 2026-03-31 091941" src="https://github.com/user-attachments/assets/50ed9623-7714-43df-aa96-cebaa61f83c4" />

<img width="1617" height="1119" alt="Screenshot 2026-03-31 091657" src="https://github.com/user-attachments/assets/cc8804d5-35f8-4fbf-bd9b-94964733befa" />


---

## Author List

- [https://github.com/bellacalicchio](https://github.com/bellacalicchio)
- [https://github.com/JoshuaVasquez2026](https://github.com/JoshuaVasquez2026)
- [https://github.com/ahassaanlatki](https://github.com/ahassaanlatki)
- [https://github.com/connorachavez](https://github.com/connorachavez)

---

## Project Scope

The scope of this project is focused on developing a four-module, self-paced AI literacy course designed for business school faculty at William & Mary's Raymond A. Mason School of Business.
The course does not aim to teach faculty how to use every AI tool available, nor does it target students, staff, or administrators. Its purpose is to educate faculty on the foundational
concepts of large language models (LLMs), address specific cognitive and ethical concerns they are most likely to have as educators, and equip them with enough knowledge to make informed
decisions about AI usage in the classroom. The final deliverable is a course website hosting all four modules, an introduction, cognitive, ethical, and summarization, for faculty to consume
at their own pace.

---

## Project Details

### Module 1: An Introduction to Artificial Intelligence

This module establishes the conceptual foundation for the entire course. First, it defines what a large language model is, distinguishing LLMs from rule-based software, search engines, and older virtual assistants.
Then, it provides a timeline of the technological evolution from the Statistical Era of the 1990s through the Neural/Transformer Revolution to the current Generative Era. Next, it discusses the most commonly used LLMs,
such as ChatGPT, Calude, Gemini, Perplexity, NotebookLM, Copilot, DeepSeek, and Grok, listing their distinctive features, educational use cases, and the organizations managing each tool. In addition, there is a prompt
engineering section that offers practical strategies for writing better prompts and grounding the model in provided context to reduce hallucinations. Also, hallucinations are directly addressed by explaining why they
occur and how newer models have significantly reduced the frequency of hallucinations. Lastly, faculty are given two activities using NotebookLM and their own course materials.

### Module 2: Cognitive Concerns of AI in Education

This module addresses six cognitive risks of AI overuse in student populations: cognitive offloading, reduced critical thinking, decline in creativity, shortened attention spans, weakened knowledge retention, and erosion
of foundation academic skills. Each of these risks is grounded in peer-reviewed research and illustrated with real-world classroom scenarios, such as a student submitting an AI generated essay. This module concludes with
three potential mitigation strategies: positioning AI as a support tool rather than a replacement for student effort, building AI literacy and critical thinking habits, and designing assessments that reduce AI dependency.
Lastly, there are reflection activities that encourage faculty to think about their current relationship with AI tools.

### Module 3: The Ethics of AI in Education

This module addresses the broader ethical landscape of AI in education. It opens with three major ethical problem areas: job displacement, environmental costs, and privacy/security risks. Then, it introduces Luciano Floridi's
five-principle ethics framework that includes Beneficence, Nonmaleficence, Autonomy, Justice, and Explicability with educational examples of each. It closes with a philosophically exploratory section on AI and humanity, posing
questions about consciousness, art, emotional connection, and what it means when AI can evoke genuine feeling without a human behind it. Lastly, a comparative activity asks faculty to write about their own definition of humanity,
share it with someone, and then discuss it with an AI model. This will allow them to experience the difference firsthand.

### Module 4: Summary & Model Guide

This module provides a review of the entire course and a reference guide for AI model selection for faculty members. A comparison table is given that covers seven major AI tools, ChatGPT, Claude, Perplexity, NotebookLM, Gemini,
DeepSeek, and Copilot, evaluating each on strengths, weaknesses, educational uses, and specific concerns. In addition, this module includes a structured prompting guide with contextual and role-based prompt examples that can be
applied to the activities found later on in the module. The two activities guide faculty through using learning-mode in an AI model (Claude or Gemini) with their own course materials and building a NotebookLM notebook from their
existing lecture content.

### Technical Aspects

We combined all of these modules into a website that contains a Home Page with an introduction, an About Us page that lists our contact information, a Course Page that contains the modules each with their own dedicated subpage
including a written description, estimated completion time, and a downloadable PowerPoint file, and a Feedback Page with a link to a survey where faculty can share their thoughts about the course. The website also features a
dedicated AI Assistant page and an AI chat button powered by a LangChain multi-agent system, where faculty can ask questions about AI concepts and receive responses grounded in verified sources. The system consists of three agents: an AIAgent that
explains concepts, a WebsiteAgent that finds credible sources using the Tavily API, and an OrchestratorAgent that coordinates both, all powered by Google's Gemini 2.5 Flash model. The website was built using HTML, CSS, and
JavaScript for the front end and Python with Flask for the back end, and styled with William & Mary's official colors to maintain a professional academic aesthetic. It is deployed on Render and connected to Github so that
any updates are automatically reflected on the live site, making it publicly accessible to faculty at any time from any device.

---

## What's Next?

We believe that there are many natural extensions to this project. First, we could create more modules to expand the course. For example, a fifth module could discuss academic integrity and AI detection tools because we believe
that this is another concern that some faculty possess. Since we did not have much time to dive deep into the four modules we already have, we believe that there is a lot of potential for expansion as a whole. Second, we could
add reference cards for each AI tool covered in Module 4 that contain more information as well as links to videos and articles. This would give faculty a more comprehensive view of the models and allow them to make better decisions
when utilizing AI. In addition to this, it is important to note that this information will need to be edited consistently due to the constantly changing AI landscape. Third, we believe that there is a potential to create sub-modules
that are specific to certain departments or courses. This could function as a place where faculty share what they have tried and what has worked versus what has not in order to provide more structured feedback with the Business School
as well as share with their peers.

---

## Responsible AI Considerations

Throughout the development of this course, our team was intentional about using AI responsibly in many ways. First, we are transparent about AI's role in building this course. This course was built with the help of AI tools, and we are
stating this here to be open about our AI usage since this is something that the course asks of students and faculty, and we hold ourselves to the same standard. Second, we verified all AI-generated content since AI was used to develop
the course as previously mentioned. This ensured that we did not take AI output at face value, which is consistent with the hallucination awareness we teach in Module 1. Third, we were mindful of access and equity when designing the
activities within the modules as we primarily focused on AI models that William & Mary students and staff had access to, such as Gemini, Claude, and NotebookLM. This way, no faculty member needed to pay to complete the course. Fourth,
the AI Assistant chat feature built into the website was developed with the same responsible AI principles taught throughout the course. The assistant includes safety guardrails that prevent fabricated citations, requires WebsiteAgent to
verify claims with real sources through the Tavily API, and is designed to supplement faculty learning rather than replace it. The system was also built with human oversight in mind, all agent behavior was reviewed and approved by our
team before deployment.

---

## References

### Relevant Research Paper

- Dr. Chung's Ethics, Responsibility, & Risk (Chapter 12 from AI for Business in Python)

### Other References

- [What Is a Large Language Model? — Cloudflare Learning Center](https://www.cloudflare.com/learning/ai/what-is-large-language-model/)
- [Introducing the Claude 3 Model Family — Anthropic](https://www.anthropic.com/news/claude-3-family)
- [DeepSeek](https://www.deepseek.com/)
- [Our Next-Generation Gemini Model — Google Blog](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/)
- [NotebookLM — Google](https://notebooklm.google/)
- [Microsoft Copilot](https://www.microsoft.com/en-us/microsoft-copilot)
- [Why Language Models Hallucinate — OpenAI](https://openai.com/index/why-language-models-hallucinate/)
- [Perplexity Pages](https://www.perplexity.ai/hub/blog/perplexity-pages)
- [YouTube Education](https://www.youtube.com/watch?v=sg_fuEzFw0g)
- [Attention Is All You Need — Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762)
- [Students' Writing Skills and Creativity in the Age of Artificial Intelligence — Bal & Arseven (2025)](https://doi.org/10.1016/j.tsc.2025.102118)
- ["So What If ChatGPT Wrote It?" Multidisciplinary Perspectives on Generative Conversational AI — Dwivedi et al. (2023)](https://doi.org/10.1016/j.ijinfomgt.2023.102642)
- [AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking — Gerlich (2025)](https://doi.org/10.3390/soc15010006)
- [ChatGPT Produces More "Lazy" Thinkers: Evidence of Cognitive Engagement Decline — Georgiou (2025)](https://arxiv.org/abs/2507.00181)
- [ChatGPT for Good? On Opportunities and Challenges of Large Language Models for Education — Kasneci et al. (2023)](https://doi.org/10.1016/j.lindif.2023.102274)
- [The Effect of ChatGPT on Students' Learning Performance, Learning Perception, and Higher-Order Thinking: A Meta-Analysis (2025)](https://doi.org/10.1057/s41599-025-04787-y)
- [The Ethics of Artificial Intelligence: Principles, Challenges, and Opportunities — Oxford Academic](https://academic.oup.com/book/46748)
- [The Carbon Footprint of AI — Climate Impact](https://www.climateimpact.com/news-insights/insights/carbon-footprint-of-ai/)
- [Explained: The Environmental Impact of Generative AI — MIT News](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)
- [AI Prompt Engineering Isn't the Future — Harvard Business Review](https://hbr.org/2023/06/ai-prompt-engineering-isnt-the-future)
- [Contextual Prompts — Sand Garden](https://www.sandgarden.com/learn/contextual-prompts)
- [Choosing the Right AI Model: A Practical Comparison — LinkedIn](https://www.linkedin.com/pulse/choosing-right-ai-model-practical-comparison-randy-haas-jofnc/)
- [LLM Leaderboard — Vellum AI](https://www.vellum.ai/llm-leaderboard?utm_source=google&utm_medium=organic)
