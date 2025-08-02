from pathlib import Path


class Directory :
    data_repo = Path('/Users/mmir/Library/CloudStorage/Dropbox/git/i58_g3_g4_CF')

    inp = data_repo / 'inp'
    med = data_repo / 'med'
    out_tbl = data_repo / 'out_tbl'


class FilePath :
    d = Directory()

    all_apps_wide_csv_250301 = d.inp / 'all_apps_wide_2025-03-01.csv'
    final_payments = d.inp / 'Final Payments.xlsx'

    clean_all_apps = d.med / 'clean_all_apps.xlsx'

    page_times = d.inp / 'PageTimes-2025-03-01.csv'
    cln_page_times = d.med / 'cln_page_times.xlsx'

    m3__participant_code_track_map = d.med / 'm3__participant_code_track_map.xlsx'
    m4__total_track_time = d.med / 'm4__total_track_time.xlsx'

    t1__survey_times_by_track_and_all__tex = d.out_tbl / 't1__survey_times_by_track_and_all.tex'
    t2__payments__xlsx = d.out_tbl / 't2__payments.xlsx'
    t3__payments__tex = d.out_tbl / 't3__payments.tex'


class Constants :
    mturk_id = 'Introduction.1.player.MTurk_ID'
    participant_payoff = 'participant.payoff'
    participant_bonus = 'participant.bonus'
    participant_code = 'participant.code'
    workerId = 'workerId'
    base = 'Base'
    bonus = 'Bonus'
    total = 'Total'
    test = 'test'
    page_index = 'page_index'
    dur_s = 'dur_s'
    epoch_time_completed = 'epoch_time_completed'
    total_track_time_sec = 'total_track_time_sec'
    participant_sni_treatment = "participant.sni_treatment"
    participant_track = "participant.track"
    track = "track"
    cl = 'Comparison Large'
    csi = 'Comparison Small Incentivized'
    csu = 'Comparison Small Unincentivized'
    tl = 'Tranisitivity Large'
    tsi = 'Transitivity Small Incentivized'
    tsu = 'Transitivity Small Unincentivized'
    track_abbreviation = 'track_abbreviation'
    total_track_time_min = 'total_track_time_min'


class Parameters :
    pass
