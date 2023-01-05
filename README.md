# `geldaq` – Data acquisition for PVC gel experiments

I'm making a modification here.

This tool facilitates the logging and display of sub-millivolt signals in the lab, such as those from PVC gels. It also provides utilities for active feedback control of systems including PVC gels and other such samples.

## Development

### Set up a quick search to LabJack documentation

Google Chrome and some other Chromium-based browsers support setting up custom site searches that allow you to quickly search documentation via typing a shortcut in the search bar. To set this up, right-click in the URL bar, click "Manage search engines and site search," click "Add" under the "Site search" section, and create a custom search for LabJack documentation

- Search engine: `LabJack`
- Shortcut: `lj`
- Url with `%s` in place of query: `https://www.google.com/search?q=site%3Ahttps%3A%2F%2Flabjack.com%2Fpages+%s`

Save this custom search engine, and now when you click in the search bar (or use Alt+D), then type "lj" (or whatever you set the shortcut to), and press spacebar, your query will search just the LabJack documentation. Be wary that some documentation is only relevant to certain hardware, and I haven't yet found how to filter this query down to the T7 hardware we are currently using.

### Adapt the LabJack examples

The `examples` directory contains usage examples from LabJack Corporation, obtained from the [Python for LJM] documentation. The syntax and style of these examples differ from our code style, so you may need to adjust them in your usage. Migrate relevant code snippets to the `src/geldaq` folder, modifying them as you see fit.

[python for ljm]: https://labjack.com/pages/support/software/?doc=/software-driver/example-codewrappers/python-for-ljm-windows-mac-linux/
