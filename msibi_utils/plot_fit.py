import os.path

from msibi_utils.parse_logfile import parse_logfile


def plot_pair_fits(pair, fits, use_agg=False, ylims=(0, 1)):
    if use_agg:
        import matplotlib as mpl
        mpl.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    for state, fit in fits[pair].items():
        d_fit = float(fit[-1]) - float(fit[-2])
        ax.plot(fit, label='{0}, \u0394f = {1:.3f}'.format(state, d_fit))
    ax.set_xlabel('step')
    ax.set_ylabel('relative fit')
    ax.set_ylim(ylims)
    ax.legend(loc='best')
    ax.set_title(pair)
    fig.tight_layout()
    fig.savefig('figures/%s-fit.pdf' % pair, transparent=True)
    plt.close('all')

def plot_all_fits(filename, use_agg=False, ylims=(-1, -1)):
    """Plot fitness function vs. iteration for each pair at each state

    Args
    ----
    filename : str
        Name of file from which to read.
    use_agg : bool
        Use Agg backend if True - may be useful on clusters with no display
    ylims : iterable, len=2
        Set the ylimits of the f_fit axes - useful for comparing plots of different pairs

    Returns
    -------
    Nothing is returned, but plots are made for each pair.

    If the directory './figures' does not exist, it is created, and the figures 
    are saved in that directory with the name 'type1-type2-fit.pdf'.
    The filename should where the optimization output was redirected, as the 
    format is determined by the MSIBI.optimize() function.
    """
    fits = parse_logfile(filename)
    if not os.path.exists('figures'):
        os.makedirs('figures')
    for pair in fits:
        plot_pair_fits(pair, fits, use_agg, ylims)
