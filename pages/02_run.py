import streamlit as st
from autogen import Agent
from autogen.agentchat import UserProxyAgent, AssistantAgent, GroupChat, GroupChatManager
from autogen.oai.openai_utils import config_list_from_json
import warnings
from promptflow.tracing import start_trace

import streamlit.components.v1 as components
def mermaid(placeholder, code: str) -> None:
    with placeholder:
        components.html(
            f"""
            <pre class="mermaid">
                {code}
            </pre>
            <script type="module">
               import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
               mermaid.initialize({{ startOnLoad: true}});
            </script>
            """, height=250
        )
        return placeholder
    
def display_graph(placeholder, active_node=None):
    nodes = []
    