# -*- coding: utf-8 -*-
import pandas as pd
import pypistats
import neurokit2 as nk



def pypi_downloads(package="name_of_the_package_on_pypi"):
    """Access the downloads history from pypi

    Examples
    ---------
    >>> import popularipy
    >>> data = popularipy.pypi_downloads("neurokit2")
    >>> data.plot(x="Date")
    """

    data = pypistats.overall(package, total=True, format="pandas")

    # process
    data = data.groupby("date").sum().sort_values("date").reset_index()
    data = data.rename(columns={"downloads": "Downloads"})
    data["Trend"] = nk.fit_loess(data["Downloads"])
    data["Date"] = pd.to_datetime(data["date"]).dt.strftime('%d %b %Y')
    return data