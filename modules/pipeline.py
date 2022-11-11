from absl import logging
from tfx.orchestration import metadata, pipeline


def init_pipeline(args):
    logging.info(f"Pipeline root set to: {args['pipeline_root']}")

    beam_args = [
        "--direct_running_mode=multi_processing",
        "----direct_num_workers=0",
    ]

    return pipeline.Pipeline(
        pipeline_name=args["pipelane_name"],
        pipeline_root=args["pipeline_root"],
        components=args["components"],
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            args["metadata_path"],
        ),
        eam_pipeline_args=beam_args,
    )
