DEFAULT_AUTHOR = "Sebastián Aedo – http://saedo.me"

def set_title(ax, title, subtitle, caption='', author=DEFAULT_AUTHOR):
    scale = 8/ax.figure.get_figheight()

    delta = 0
    va = 'top'
    if subtitle != "":
        delta = 0.01
        va = 'bottom'

    # bigger title
    ax.text(0, 1 + (.05 + delta)*scale,
            title, va=va,
            transform=ax.transAxes,
            fontsize=20, fontweight='semibold')
    # subtitle
    ax.text(0, 1 + .05*scale,
            subtitle,
            fontsize=17,
            va='top',
            transform=ax.transAxes, fontweight='light', alpha=0.7)

    #caption below
    ax.text(0, -0.15*scale, caption, fontsize=17, transform=ax.transAxes,
            fontweight="light")

    ax.text(1, -0.1*scale, author,
            transform=ax.transAxes, alpha=0.7, fontweight='regular', ha='right')

def savefig(fig, filename, dpi=300):
    fig.savefig(filename, dpi=dpi, bbox_inches='tight')
