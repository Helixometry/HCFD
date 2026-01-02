// Healthcare CodecFake manifest (dummy examples)
// You can keep extra fields (split/protocol/speaker_id/codec_family etc.) — site only uses:
// codec, gt_id, gt_url, gen_url, condition
window.MANIFEST_RAW = [
  {
    id: "dep_utt_0001",
    gt_id: "dep_utt_0001",
    gt_url: "audio/real/depression/dep_utt_0001.wav",
    gen_url: "audio/generated/depression/Encodec_24kHz/dep_utt_0001.wav",
    condition: "Depression",
    codec: "Encodec_24kHz",
    split: "test",
    protocol: "seen",
    speaker_id: "spk_001",
    codec_family: "Encodec"
  },
  {
    id: "dys_utt_0042",
    gt_id: "dys_utt_0042",
    gt_url: "audio/real/dysarthria/dys_utt_0042.wav",
    gen_url: "audio/generated/dysarthria/SpeechTokenizer/dys_utt_0042.wav",
    condition: "Dysarthria",
    codec: "SpeechTokenizer",
    split: "val",
    protocol: "unseen",
    speaker_id: "spk_019",
    codec_family: "Tokenizer"
  },
  {
    id: "alz_utt_0107",
    gt_id: "alz_utt_0107",
    gt_url: "audio/real/alzheimer/alz_utt_0107.wav",
    gen_url: "audio/generated/alzheimer/SNAC_44kHz/alz_utt_0107.wav",
    condition: "Alzheimer",
    codec: "SNAC_44kHz",
    split: "test",
    protocol: "seen",
    speaker_id: "spk_203",
    codec_family: "SNAC"
  }
];
