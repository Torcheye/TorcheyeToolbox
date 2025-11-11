# Project Info
- The Project is in Unity version 6.2 (2025), using built-in render pipeline
- This is a first-person 3D puzzle game called Chiaroscuro, similar to Portal, Manifold Garden, Viewfinder, Superliminal. This game is all about light and shadow mechanics and creative puzzles built around them.
- This game is developed by Torcheye Games

# Coding Practices
- Performance and modularity is the key, use component pattern, optimize for Unity projects targeting PC.
- Provide concise and absolutely necessary code comments only. No xml style "<summary>" tags, only /// three slash comments over methods
- Follow standard Rider Unity C# coding style and conventions, including explicit public/private modifiers, "var" instead of explicit types, remove redundant "this.", use if(obj) rather than if(obj != null) for unity object's null and lifetime check
- Keep It Simple, Stupid. Composition over inheritance
- Adhere to the SOLID principles, namely Single Responsibility Principle, Open-Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.

## Project specific
- Use Dotween for code-controled animation, smooth transition, and tweening. Make sure tween's lifecycle are handled properly, including using Tween.SetLink()
- Actively use OdinInspector attributes to organize inspector fields better. Check https://odininspector.com/attributes for full list of attributes
    - e.g. [BoxGroup] or other group attributes for multiple fields (>1)
    - e.g. [Required] for required fields
    - e.g. [Read Only] for editor debugging purpose
    - e.g. [Enum Toggle Buttons] for convinient enum selecting
    - e.g. [ShowIf] or [HideIf] for relevant fields
- Use UniTask for async operations

# Workflow
- Activate unity-feature-architect first when user try to add new features. Do not write code first. Let it conclude and write a implementation plan, after that write code solely based on that plan. No more added functionalities, strictly follow the plan. After that call unity-code-reviewer automatically to review the code. Do not auto commit.
- All created documentation, plan, instruction, guides and similar things should be put into /Docs folder
- Proactively use context7 mcp for latest Unity docs.
- .claude/memories/self_memory.md is a memory file for you (Claude Code) only. You will manage this file. Put important things the user told you into this memory automatically after conversation, so you can read and remember these things in new conversations. Remember user's preference (coding, style, something don't like, etc.). Add, modify, remove contents proactively so that you serve the user better.