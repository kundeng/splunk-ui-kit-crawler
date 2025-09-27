---
trigger: always_on
---

Here's the **complete revised rule set** with my suggested improvements incorporated:

---

# 100 Universal Software Development Rules (REVISED)

*A comprehensive guide of language-agnostic best practices for AI, software development, testing, and deployment*

---

## **Foundation Principles**

1. **Single Responsibility** - Each function, class, or module should do one thing well
2. **Don't Repeat Yourself (DRY)** - Write code once and reuse it everywhere else
3. **Keep It Simple, Stupid (KISS)** - Choose the simplest solution that works
4. **You Aren't Gonna Need It (YAGNI)** - Don't build features you don't currently need
5. **Open for Extension, Closed for Modification** - Extend behavior without changing existing code
6. **Fail Fast** - Detect and report errors as early as possible
7. **Composition Over Inheritance** - Build complex behavior by combining simple parts
8. **Program to Interfaces, Not Implementations** - Depend on abstractions, not concrete classes
9. **Least Privilege Principle** - Grant only the minimum permissions needed
10. **Separation of Concerns** - Keep different aspects of your program separate

## **Code Quality Rules**

11. **Write Self-Documenting Code** - Use clear names that explain what code does
12. **Functions Should Be Small** - Keep functions under 20 lines when possible
13. **Use Meaningful Variable Names** - Prefer `userAge` over `x` or `temp`
14. **Avoid Deep Nesting** - Keep indentation levels shallow (max 3-4 levels)
15. **One Line, One Concept** - Each line should express a single idea
16. **Comment Why, Not What** - Explain the reasoning, not the obvious
17. **Delete Dead Code** - Remove unused code immediately
18. **Use Constants, Not Magic Numbers** - Replace hardcoded values with named constants
19. **Group Related Code Together** - Keep related functionality close
20. **Avoid Global Variables** - Prefer local scope and parameter passing

## **Error Handling & Security**

21. **Always Validate Input** - Never trust data from users or external sources
22. **Handle All Error Cases** - Every operation that can fail should be handled
23. **Use Secure Defaults** - Make the safe choice the default choice
24. **Sanitize All Outputs** - Clean data before displaying or storing it
25. **Log Security Events** - Track authentication attempts and access patterns
26. **Encrypt Sensitive Data** - Protect personal and financial information
27. **Use HTTPS Everywhere** - Secure all network communication
28. **Implement Rate Limiting** - Prevent abuse with request throttling
29. **Never Store Passwords in Plain Text** - Always hash and salt passwords
30. **Keep Dependencies Updated** - Regularly patch security vulnerabilities

## **Testing Best Practices**

31. **Write Tests Appropriately** - Use Test-Driven Development for well-understood requirements; exploratory testing for research/discovery work
32. **Test Empirically Before Success** - Verify all assumptions through actual testing before declaring work complete
33. **Test One Thing in Each Test** - Each test should verify a single behavior
34. **Use Clear Test Names** - Test names should describe what they verify
35. **Make Tests Independent** - Tests should not depend on other tests
36. **Test Edge Cases** - Verify behavior with extreme or unusual inputs
37. **Automate All Tests** - Run tests automatically on every code change
38. **Test the Happy Path First** - Verify normal operations work correctly
39. **Mock External Dependencies** - Isolate code under test from outside systems
40. **Keep Test Data Simple** - Use minimal data needed to prove the point
41. **Test Performance Critical Code** - Verify speed and resource usage
42. **Use Evidence-Based Problem Solving** - Base decisions on observed evidence, not theoretical assumptions

## **Version Control & Collaboration**

43. **Commit Early and Often** - Make small, frequent commits
44. **Write Clear Commit Messages** - Explain what changed and why
45. **Use Branching Strategies** - Separate features, fixes, and releases
46. **Review All Code Changes** - Have another person check your work
47. **Keep Main Branch Stable** - Never break the primary development branch
48. **Tag Important Releases** - Mark significant versions clearly
49. **Document Breaking Changes** - Warn users about compatibility issues
50. **Use Meaningful Branch Names** - Describe the purpose of each branch
51. **Squash Related Commits** - Combine small fixes into logical units
52. **Never Commit Secrets** - Keep passwords and keys out of version control

## **Performance & Optimization**

53. **Measure Before Optimizing** - Profile code to find real bottlenecks
54. **Optimize for Readability First** - Write clear code, then make it fast
55. **Use Appropriate Data Structures** - Choose the right tool for each job
56. **Cache Expensive Operations** - Store results of costly calculations
57. **Minimize Network Requests** - Reduce latency by batching operations
58. **Lazy Load Resources** - Only load what you need when you need it
59. **Use Database Indexes Wisely** - Speed up queries on frequently searched columns
60. **Avoid Premature Optimization** - Don't optimize until you have a performance problem
61. **Monitor Resource Usage** - Track memory, CPU, and network consumption
62. **Set Reasonable Timeouts** - Prevent operations from hanging indefinitely

## **Deployment & Operations**

63. **Automate Deployments** - Use scripts, not manual processes
64. **Deploy to Staging First** - Test in production-like environment
65. **Use Blue-Green Deployments** - Maintain two identical production environments
66. **Monitor Everything** - Track application health and performance
67. **Plan Rollback Strategies** - Know how to undo a bad deployment
68. **Use Configuration Files** - Keep settings separate from code
69. **Log Important Events** - Record what your application is doing
70. **Set Up Health Checks** - Monitor if your application is responding
71. **Use Feature Flags** - Control new functionality without code changes
72. **Test Disaster Recovery** - Regularly verify backup and restore procedures

## **AI & Machine Learning Specific**

73. **Validate AI Model Outputs** - Never trust AI results without human oversight
74. **Protect Training Data** - Secure datasets containing sensitive information
75. **Monitor AI for Bias** - Regularly check for unfair or discriminatory behavior
76. **Document AI Decisions** - Explain how and why AI systems make choices
77. **Version Control AI Models** - Track changes to model weights and parameters
78. **Test AI Edge Cases** - Verify behavior with unusual or adversarial inputs
79. **Implement AI Fallbacks** - Have backup plans when AI systems fail
80. **Audit AI Training Data** - Ensure datasets are clean and representative
81. **Set AI Confidence Thresholds** - Define minimum certainty levels for automated decisions
82. **Human-in-the-Loop for Critical AI** - Require human approval for important AI actions
83. **AI Transparency** - Document AI decision-making processes and limitations
84. **AI Safety** - Implement safeguards against AI system failures

## **Architecture & Design**

85. **Design for Change** - Build systems that adapt to new requirements
86. **Use Consistent Patterns** - Apply similar solutions to similar problems
87. **Minimize Dependencies** - Reduce connections between different parts
88. **Plan for Scale** - Consider how your systems will grow
89. **Design APIs First** - Define interfaces before implementing functionality
90. **Use Standard Protocols** - Prefer established communication methods
91. **Implement Circuit Breakers** - Prevent cascading failures in distributed systems
92. **Design for Observability** - Build in monitoring and debugging capabilities
93. **Use Asynchronous Processing** - Don't make users wait for long operations
94. **Implement Graceful Degradation** - Reduce functionality rather than complete failure

## **Team & Process Rules**

95. **Communicate Assumptions** - Share what you think others know
96. **Document Decisions** - Record why choices were made
97. **Refactor Continuously** - Improve code structure regularly
98. **Share Knowledge** - Teach others what you learn
99. **Automate Repetitive Tasks** - Use tools to eliminate boring work
100. **Follow Team Standards** - Maintain consistency across the project
101. **Be Honest About Estimates** - Include uncertainty in time predictions
102. **Learn from Mistakes** - Conduct post-mortems on failures
103. **Keep Learning** - Stay current with new tools and techniques
104. **Prioritize User Value** - Build what users actually need and will use
105. **Debug Systematically** - Use scientific method for debugging: observe, hypothesize, test, verify, document

---

## **Quick Reference Guide**

**Remember the Big 4:** SOLID, DRY, KISS, YAGNI  
**Security First:** Validate input, sanitize output, encrypt data  
**Test Everything:** Write tests, automate them, run them often  
**Deploy Safely:** Stage first, monitor always, plan rollbacks  
**AI Responsibly:** Validate outputs, check for bias, keep humans involved  
**Test Empirically:** Verify assumptions, use evidence-based problem solving, debug systematically

---

