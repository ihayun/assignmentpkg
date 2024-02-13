# Github API analysis project
This package is to determine mean, max, and min forks from the top 20 stars git repositories

# Install
    !pip install git+https://github.com/user/assignmentpkg
    from assignmentpkg import Analysis
    analysis_obj = Analysis.Analysis('config.yml')
    analysis_obj.load_data()
    analysis_output = analysis_obj.compute_analysis()
    print(analysis_output)
    analysis_figure = analysis_obj.plot_data()

# Requirements
Put your github token into the user_config.yml
