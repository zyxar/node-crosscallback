{
  'targets': [{
    'target_name': 'addon',
    'sources': [
      'addon.cc',
      'Event.cc',
      "<!(node -e \"require('..')\")/async/Argument.cc",
      "<!(node -e \"require('..')\")/async/NodeEventEmitter.cc",
      "<!(node -e \"require('..')\")/async/EventEmitterObjectWrap.cc",
    ],
    'include_dirs' : [ "<!(node -e \"require('..')\")" ],
    'conditions': [
      [ 'OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',       # -fno-exceptions
          'GCC_ENABLE_CPP_RTTI': 'YES',             # -fno-rtti
          'MACOSX_DEPLOYMENT_TARGET' : '10.7',      # from MAC OS 10.7
          'OTHER_CFLAGS': [
            '-g -O3 -stdlib=libc++ -std=c++11',
          ]
        },
      }, { # OS!="mac"
        'cflags!':    ['-fno-exceptions'],
        'cflags':     ['-D__STDC_CONSTANT_MACROS'],
        'cflags_cc':  ['-Wall', '-O3', '-g' , '-std=c++11', '-fexceptions'],
        'cflags_cc!': ['-fno-exceptions'],
        'cflags_cc!': ['-fno-rtti'],
      }],
    ]
  }]
}
