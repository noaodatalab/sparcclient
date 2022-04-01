from collections import OrderedDict


boss_json = ['_dr',
 'dec',
 'ra',
 'redshift',
 'specid',
 'spectra.coadd.FLUX',
 'spectra.coadd.IVAR']

boss_numpy = ['_dr', 'nparr']

boss_pandas = ['_dr', 'df']

boss_spectrum1d = ['_dr', 'redshift', 'spec1d']

boss_spectrum1d_redshift = 0.570779085159302
everest_numpy = ['_dr', 'dec', 'nparr', 'ra', 'specid']

everest_pandas = ['_dr', 'b_df', 'r_df', 'z_df']

everest_spectrum1d = ['_dr', 'b_spec1d', 'r_spec1d', 'z_spec1d']

everest_b_spectrum1d_redshift = 0.17526327367673789

fields_available = {'BOSS-DR16': ['_dr', 'flux', 'id', 'wavelength']}

record_examples = {'BOSS-DR16': ['_dr',
               'data_release_id',
               'datasetgroup_id',
               'dec',
               'ra',
               'redshift',
               'specid',
               'spectra.coadd.FLUX',
               'spectra.coadd.IVAR',
               'spectra.coadd.LOGLAM']}

get_vectordata  = ['flux', 'and_mask', 'ivar', 'loglam']

get_metadata  = [{'FIBERID': 892,
  'MJD': 58466,
  'PLATEID': 10660,
  'RUN1D': 'v5_13_0',
  'RUN2D': 'v5_13_0',
  'SPECOBJID': 12002338340072607744,
  '_dr': 'BOSS-DR16',
  'data_release_id': 'BOSS-DR16',
  'datasetgroup_id': 'SDSS_BOSS',
  'dec': 28.751204,
  'filename': 'spec-10660-58466-0892.fits',
  'filesize': 218880,
  'instrument_id': 'BOSS',
  'ra': 133.46096,
  'redshift': -0.00413607759401202,
  'redshift_err': -1.0,
  'redshift_warning': 5,
  'site_id': 'apo',
  'specid': 1429933274376612,
  'specprimary': True,
  'spectype_id': 'STAR',
  'targetid': 0,
  'telescope_id': 'sloan25m',
  'wavemax': 10356.189453125,
  'wavemin': 3601.63745117188}]

rename_fields = ['_dr', 'data_set', 'f', 'ivar', 'loglam', 'specid', 'x', 'y', 'z']
rename_fields_internal = ['_dr', 'data_release_id', 'f2', 'redshift', 'specid', 'spectra.coadd.IVAR', 'spectra.coadd.LOGLAM', 'x', 'y']


get_field_names_internal = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 '_dr',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

get_field_names = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 '_dr',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

orig_field = 'flux'
client_field = 'flux'

normalize_field_names = [['_dr', 'flux', 'ivar']]

df_lut_internal=OrderedDict([('FIBERID', {'default': False, 'new': 'FIBERID'}),
             ('MJD', {'default': False, 'new': 'MJD'}),
             ('PLATEID', {'default': False, 'new': 'PLATEID'}),
             ('RUN1D', {'default': False, 'new': 'RUN1D'}),
             ('RUN2D', {'default': False, 'new': 'RUN2D'}),
             ('SPECOBJID', {'default': False, 'new': 'SPECOBJID'}),
             ('_dr', {'default': True, 'new': '_dr'}),
             ('data_release_id', {'default': False, 'new': 'data_release_id'}),
             ('datasetgroup_id', {'default': False, 'new': 'datasetgroup_id'}),
             ('dateobs', {'default': False, 'new': 'dateobs'}),
             ('dateobs_center', {'default': False, 'new': 'dateobs_center'}),
             ('dec', {'default': False, 'new': 'dec'}),
             ('dirpath', {'default': False, 'new': 'dirpath'}),
             ('exptime', {'default': False, 'new': 'exptime'}),
             ('extra_files', {'default': False, 'new': 'extra_files'}),
             ('filename', {'default': False, 'new': 'filename'}),
             ('filesize', {'default': False, 'new': 'filesize'}),
             ('flux', {'default': True, 'new': 'flux'}),
             ('id', {'default': True, 'new': 'id'}),
             ('instrument_id', {'default': False, 'new': 'instrument_id'}),
             ('ivar', {'default': False, 'new': 'ivar'}),
             ('mask', {'default': False, 'new': 'mask'}),
             ('model', {'default': False, 'new': 'model'}),
             ('ra', {'default': False, 'new': 'ra'}),
             ('redshift', {'default': False, 'new': 'redshift'}),
             ('redshift_err', {'default': False, 'new': 'redshift_err'}),
             ('redshift_warning',
              {'default': False, 'new': 'redshift_warning'}),
             ('site_id', {'default': False, 'new': 'site_id'}),
             ('sky', {'default': False, 'new': 'sky'}),
             ('specid', {'default': False, 'new': 'specid'}),
             ('specprimary', {'default': False, 'new': 'specprimary'}),
             ('spectype_id', {'default': False, 'new': 'spectype_id'}),
             ('targetid', {'default': False, 'new': 'targetid'}),
             ('telescope_id', {'default': False, 'new': 'telescope_id'}),
             ('wave_sigma', {'default': False, 'new': 'wave_sigma'}),
             ('wavelength', {'default': True, 'new': 'wavelength'}),
             ('wavemax', {'default': False, 'new': 'wavemax'}),
             ('wavemin', {'default': False, 'new': 'wavemin'})])

df_lut=OrderedDict([('FIBERID', {'default': False, 'new': 'FIBERID'}),
             ('MJD', {'default': False, 'new': 'MJD'}),
             ('PLATEID', {'default': False, 'new': 'PLATEID'}),
             ('RUN1D', {'default': False, 'new': 'RUN1D'}),
             ('RUN2D', {'default': False, 'new': 'RUN2D'}),
             ('SPECOBJID', {'default': False, 'new': 'SPECOBJID'}),
             ('_dr', {'default': True, 'new': '_dr'}),
             ('data_release_id', {'default': False, 'new': 'data_release_id'}),
             ('datasetgroup_id', {'default': False, 'new': 'datasetgroup_id'}),
             ('dateobs', {'default': False, 'new': 'dateobs'}),
             ('dateobs_center', {'default': False, 'new': 'dateobs_center'}),
             ('dec', {'default': False, 'new': 'dec'}),
             ('dirpath', {'default': False, 'new': 'dirpath'}),
             ('exptime', {'default': False, 'new': 'exptime'}),
             ('extra_files', {'default': False, 'new': 'extra_files'}),
             ('filename', {'default': False, 'new': 'filename'}),
             ('filesize', {'default': False, 'new': 'filesize'}),
             ('flux', {'default': True, 'new': 'flux'}),
             ('id', {'default': True, 'new': 'id'}),
             ('instrument_id', {'default': False, 'new': 'instrument_id'}),
             ('ivar', {'default': False, 'new': 'ivar'}),
             ('mask', {'default': False, 'new': 'mask'}),
             ('model', {'default': False, 'new': 'model'}),
             ('ra', {'default': False, 'new': 'ra'}),
             ('redshift', {'default': False, 'new': 'redshift'}),
             ('redshift_err', {'default': False, 'new': 'redshift_err'}),
             ('redshift_warning',
              {'default': False, 'new': 'redshift_warning'}),
             ('site_id', {'default': False, 'new': 'site_id'}),
             ('sky', {'default': False, 'new': 'sky'}),
             ('specid', {'default': False, 'new': 'specid'}),
             ('specprimary', {'default': False, 'new': 'specprimary'}),
             ('spectype_id', {'default': False, 'new': 'spectype_id'}),
             ('targetid', {'default': False, 'new': 'targetid'}),
             ('telescope_id', {'default': False, 'new': 'telescope_id'}),
             ('wave_sigma', {'default': False, 'new': 'wave_sigma'}),
             ('wavelength', {'default': True, 'new': 'wavelength'}),
             ('wavemax', {'default': False, 'new': 'wavemax'}),
             ('wavemin', {'default': False, 'new': 'wavemin'})])

retrieve_0 = ['6725afe4-a279-4103-9612-cf8dcd5e2bca', '8ad95037-d288-4bf7-84c3-5bdb010174c5']

retrieve_0b = ['flux', 'id', 'wavelength']

retrieve_4 = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

retrieve_5 = ['FIBERID',
 'MJD',
 'PLATEID',
 'RUN1D',
 'RUN2D',
 'SPECOBJID',
 'data_release_id',
 'datasetgroup_id',
 'dateobs',
 'dateobs_center',
 'dec',
 'dirpath',
 'exptime',
 'extra_files',
 'filename',
 'filesize',
 'flux',
 'id',
 'instrument_id',
 'ivar',
 'mask',
 'model',
 'ra',
 'redshift',
 'redshift_err',
 'redshift_warning',
 'site_id',
 'sky',
 'specid',
 'specprimary',
 'spectype_id',
 'targetid',
 'telescope_id',
 'wave_sigma',
 'wavelength',
 'wavemax',
 'wavemin']

find_0 = [{'ra': 208.02613,
           'id': '6ec21117-2cb3-4887-9ed9-fb1dd8dc56f5',
           'dec': -0.37900273}]
