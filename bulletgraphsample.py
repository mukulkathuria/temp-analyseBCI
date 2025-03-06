import seaborn as sns
import matplotlib.pyplot as plt


def bulletgraph(
    data=None,
    limits=None,
    labels=None,
    axis_label=None,
    title=None,
    size=(5, 3),
    palette=None,
    formatter=None,
    target_color="gray",
    bar_color="black",
    label_color="gray",
):
    """Build out a bullet graph image
    Args:
        data = List of labels, measures and targets
        limits = list of range valules
        labels = list of descriptions of the limit ranges
        axis_label = string describing x axis
        title = string title of plot
        size = tuple for plot size
        palette = a seaborn palette
        formatter = matplotlib formatter object for x axis
        target_color = color string for the target line
        bar_color = color string for the small bar
        label_color = color string for the limit label text
    Returns:
        a matplotlib figure
    """
    h = limits[-1] / 10

    if palette is None:
        palette = sns.light_palette("green", len(limits), reverse=False)

    if len(data) == 1:
        fig, ax = plt.subplots(figsize=size, sharex=True)
    else:
        fig, axarr = plt.subplots(len(data), figsize=size ,sharex=True)

    for idx, item in enumerate(data):
        if len(data) > 1:
            ax = axarr[idx]
        ax.set_aspect("equal")
        ax.set_yticklabels([item[0]], fontsize=6)
        ax.set_yticks([1])
        ax.spines["bottom"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)

        prev_limit = 0
        for idx2, lim in enumerate(limits):
            ax.barh(
                [1], lim - prev_limit, left=prev_limit, height=h, color=palette[idx2]
            )
            prev_limit = lim
        rects = ax.patches
        ax.barh([1], item[1], height=(h / 3), color=bar_color)
        ymin, ymax = ax.get_ylim()
        ax.vlines(item[2], ymin * 0.9, ymax * 0.9, linewidth=1.5, color=target_color)

    if labels is not None:
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                -height * 0.4,
                label,
                ha="center",
                va="bottom",
                color=label_color
            )
    if formatter:
        ax.xaxis.set_major_formatter(formatter)
    if axis_label:
        ax.set_xlabel(axis_label)
    if title:
        fig.suptitle(title, fontsize=14)
    fig.subplots_adjust(hspace=0)
    fig.savefig("bulletgraph1.jpg")


# data_to_plot2 = [
#     ("Age", 105, 120),
#     ("Lead Source", 99, 110),
#     ("First Time Buyer", 109, 125),
#     ("Income", 135, 123),
#     ("Gender", 45, 105),
# ]

data_to_plot2 = [
    ("Customer Profile", 99, 50),
    ("Finances", 70, 50),
    ("Booking Details", 90, 50),
    ("Delivery Details", 40, 50),
    ("Customer Details", 30, 50),
]

bulletgraph(
    data_to_plot2,
    limits=[20, 40, 80, 100],
    labels=["Poor", "OK", "Good", "Excellent"],
    size=(8, 5),
    axis_label="Performance Measure",
    label_color="black",
    bar_color="#252525",
    target_color="#f7f7f7",
    title="Total Prediction",
)
