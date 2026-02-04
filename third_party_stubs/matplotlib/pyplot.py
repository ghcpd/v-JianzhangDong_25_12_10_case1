class _FakeFigure:
    def __init__(self):
        self._saved = False
    def savefig(self, path):
        with open(path, 'wb') as f:
            f.write(b'FAKEPNG')

def figure(figsize=None):
    return _FakeFigure()

def hist(data, bins=10):
    # no-op for stub
    return

def title(t):
    return

def tight_layout():
    return

def plot_histogram(data, title=None):
    fig = figure(figsize=(6,4))
    hist(data)
    title(title)
    tight_layout()
    return fig

# Module-level convenience functions
def savefig(path):
    with open(path, 'wb') as f:
        f.write(b'FAKEPNG')

# Expose common API
plot = plot_histogram
figure = figure
hist = hist
title = title
tight_layout = tight_layout
savefig = savefig