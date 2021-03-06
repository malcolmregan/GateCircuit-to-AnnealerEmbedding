


import sys
from converter.qiskit._util import _has_connection
from ._circuit_visualization import circuit_drawer, plot_circuit, generate_latex_source,\
    latex_circuit_drawer, matplotlib_circuit_drawer, _text_circuit_drawer, qx_color_scheme
from ._error import VisualizationError
from ._state_visualization import plot_bloch_vector
from ._dag_visualization import dag_drawer

if ('ipykernel' in sys.modules) and ('spyder' not in sys.modules):
    if _has_connection('https://qvisualization.mybluemix.net/', 443):
        from .interactive._iplot_state import iplot_state as plot_state
        from .interactive._iplot_histogram import iplot_histogram as \
            plot_histogram
    else:
        from ._state_visualization import plot_state
        from ._counts_visualization import plot_histogram
else:
    from ._state_visualization import plot_state
    from ._counts_visualization import plot_histogram
