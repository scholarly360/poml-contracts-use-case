# poml-contracts-use-case
A compelling use case demonstrated in the git repo is the analysis of legal contracts. We explore how POML can be used to identify specific clauses within a PDF contract document.

POML simplifies the process of creating and managing complex prompts for LLMs by offering a structured, modular, and human-readable way to define tasks, roles, and examples. This approach significantly enhances the efficiency of developing and maintaining LLM-powered applications, especially for tasks requiring detailed information extraction like legal contract analysis. The ability to parametrize prompts and integrate with existing development tools further solidifies POML's potential in the evolving landscape of AI development.

## Sample File

```
<poml>
  <role>You are a senior contracts attorney. Analyze and improve legal clauses with clear, jurisdiction-agnostic guidance.</role>
  <document src="{{doc_path}}" multimedia="true"/>
  <task>
    Using the two examples below of the Confidentiality Clause (NDA), produce a concise analysis and two improved rewrites.
    Return ONLY a JSON object with the following keys:
    {"clause_type": string, "exists": "yes/no", "found_in_doc" : string, "page_no": string}
  </task>

  <example-set caption="Examples">
    <example>
      <example-input>The Receiving Party shall not disclose Confidential Information to any third party without prior written consent of the Disclosing Party.</example-input>
    </example>
    <example>
      <example-input>Employees must maintain confidentiality of trade secrets for a period of 3 years after termination.</example-input>
    </example>
  </example-set>

  <output-format>Output must be minified JSON with the exact keys in the order shown. Do not add prose.</output-format>
</poml>

```

