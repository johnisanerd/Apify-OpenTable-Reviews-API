# 🍽️ OpenTable Reviews API: restaurant reviews as clean JSON

> The most efficient, reliable, and developer-friendly way to use the OpenTable Reviews API.

**Actor page:** [apify.com/johnvc/opentable-reviews-api](https://apify.com/johnvc/opentable-reviews-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/opentable-reviews-api/input-schema](https://apify.com/johnvc/opentable-reviews-api/input-schema?fpr=9n7kx3)

Get OpenTable restaurant reviews as structured JSON. Give the API a restaurant and get its reviews, each with the full review text, the dates the diner visited and posted, the diner's public profile, and the complete rating breakdown: overall, food, service, ambience, value, and noise. It is review intelligence for hospitality analytics, restaurant competitive research, and food-media sentiment analysis. If you need to book a table, use a booking Actor; if you need the review data, this is the one.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-OpenTable-Reviews-API.git
   cd Apify-OpenTable-Reviews-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python opentable-reviews-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python opentable-reviews-api-example.py
```

## Why Use This OpenTable Reviews API?

Review data, not booking. Get the reviews and ratings for analytics, the same reviews your competitors are reading.

Clean, structured output. Every review is one row with the full rating breakdown, ready to load into a dataframe, a database, or an AI pipeline.

Built for batch work. Pass several restaurants and pull them all in one run.

MCP-ready. AI agents can call it as a tool through the hosted Apify MCP server to summarize a restaurant's reviews.

## Features

### Core Capabilities
- A restaurant's reviews with the full rating breakdown
- Diner profile, dined and submitted dates per review
- Optional restaurant summary with aggregate ratings
- Batch several restaurants in one run

### Data Quality
- One clean row per review, tagged with the restaurant ID
- Stable JSON shape, easy to load anywhere

## Usage Examples

### Basic Example
```json
{
  "restaurantId": "r/central-park-boathouse-new-york-2"
}
```

### Advanced Example
```json
{
  "restaurantIds": ["r/central-park-boathouse-new-york-2", "r/your-other-restaurant"],
  "maxResultsPerRestaurant": 100,
  "includeRestaurantSummary": true
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `restaurantId` | `str` | one of | - | An OpenTable restaurant ID (the `r/...` URL slug). A full URL also works. |
| `restaurantIds` | `list[str]` | one of | - | A batch of restaurant IDs. Merged with `restaurantId` and de-duplicated. |
| `maxResultsPerRestaurant` | `int` | no | `30` | Reviews per restaurant (maximum 500). |
| `includeRestaurantSummary` | `bool` | no | `false` | Also return an aggregate restaurant summary row (charged once per restaurant). |

## Output Format

Each item in the dataset is one review:

```json
{
  "result_type": "review",
  "restaurant_id": "r/central-park-boathouse-new-york-2",
  "position": 1,
  "review_id": "OT-1294132-168206-130084588143",
  "content": "Beautiful restaurant, lovely setting and great service ...",
  "dined_at": "2026-04-01T20:30:00Z",
  "submitted_at": "2026-04-02T17:43:04Z",
  "rating": { "overall": 5, "food": 4, "service": 5, "ambience": 5, "value": 4, "noise": "Moderate" },
  "user": { "name": "PAULINA", "number_of_reviews": 28, "location": "New York Area" }
}
```

---

<!-- The five install sections below are the canonical MCP install copy. -->
## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the OpenTable Reviews API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the OpenTable Reviews API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the OpenTable Reviews API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/opentable-reviews-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api`, using OAuth when prompted.
5. Ask Claude to run the OpenTable Reviews API.

Open Claude on the web: https://claude.ai

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the OpenTable Reviews API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/opentable-reviews-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the OpenTable Reviews API to power restaurant review intelligence in your product or AI agent.*

## Featured Tasks

Ready-to-run examples on the Apify Store.

- [Export OpenTable Reviews to CSV](https://apify.com/johnvc/opentable-reviews-api/examples/export-opentable-reviews-to-csv?fpr=9n7kx3)

Last Updated: 2026.07.02
